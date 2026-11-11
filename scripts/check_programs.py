"""Check the summer research list for problems before a push.

Reads opportunities/reu/programs.yml (schema in its header) and reports, one
line each:

  errors (exit 1)
    * unknown keys, so a typo such as `deadine` cannot hide
    * missing id, title, url or summer on any entry
    * an id that is not a lowercase slug, or the same id twice
    * a kind, status, applies_via or area tag outside the vocabulary
    * a flag that is not true, false or null
    * a date that is not YYYY-MM-DD, or a usual_deadline in the wrong form
    * on verified entries: a missing required field, or a deadline with no
      source_url
    * a link that fails to load (skip with --no-net)

  warnings
    * entries not verified yet (they stay out of the CSV)
    * entries last checked more than --stale days ago
    * entries still on an older summer than the current season
    * a deadline outside the year before or the year of its summer
    * the same title or program page twice
    * a link the site refused to a script (403 or 429): check it by hand

Run from the repo root:

    uv run python scripts/check_programs.py
    uv run python scripts/check_programs.py --no-net --stale 45
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

DATA = Path(__file__).resolve().parent.parent / "opportunities/reu/programs.yml"

# Every key an entry may have, in CSV order (source_url is YAML only).
KEYS = [
    "id", "title", "host", "location", "deadline", "usual_deadline",
    "season_note", "status", "kind", "area", "applies_via", "noncitizens",
    "early_years", "community_college", "apply_url", "eligibility_url",
    "projects_url", "url", "summer", "last_verified", "note", "source_url",
]
REQUIRED_ALWAYS = ["id", "title", "url", "summer"]
REQUIRED_VERIFIED = [
    "host", "location", "usual_deadline", "status", "kind", "area", "applies_via",
]
FLAGS = ["noncitizens", "early_years", "community_college"]
URL_KEYS = ["url", "apply_url", "eligibility_url", "projects_url", "source_url"]

KINDS = {"nsf-reu", "national-lab", "nasa", "other"}
STATUSES = {"confirmed", "awaiting-funding", "cancelled", "unknown"}
VIA = {"etap", "nasa-gateway", "doe-wdts", "own"}
AREAS = {
    "astronomy", "astrophysics", "planetary", "solar", "space",
    "particle", "nuclear", "condensed-matter", "optics", "amo",
    "plasma", "gravitational", "biophysics", "computational",
    "physics-general", "education",
}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MONTHS = ("January February March April May June July August "
          "September October November December").split()
USUAL_RE = re.compile(r"^(rolling|(early|mid|late) (" + "|".join(MONTHS) + "))$")


def season(today: dt.date) -> int:
    """Next summer, rolling over on August 1. Same rule as _reu.ejs."""
    return today.year + 1 if today.month >= 8 else today.year


def as_date(value) -> dt.date | None:
    """PyYAML turns unquoted dates into date objects. Accept both forms."""
    if value is None or isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


USER_AGENT = "Mozilla/5.0 (compatible; saxonstockton.com link check)"
# Politeness (Saxon, 2026-11-10: never flood a domain). Requests to one host go
# one at a time, at least --gap seconds apart. Different hosts run side by side,
# at most MAX_HOSTS_AT_ONCE of them. A 403 or 429 stops all further requests to
# that host for this run.
MAX_HOSTS_AT_ONCE = 6


def fetch(url: str) -> tuple[str, str | None, bool]:
    """(url, problem or None, problem is only a warning)."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return url, None if resp.status < 400 else f"HTTP {resp.status}", False
    except urllib.error.HTTPError as e:
        return url, f"HTTP {e.code}", e.code in (403, 429)
    except Exception as e:  # timeouts, DNS, TLS
        return url, type(e).__name__, False


def host_of(url: str) -> str:
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def check_host(urls: list[str], gap: float) -> list[tuple[str, str | None, bool]]:
    """Fetch one host's URLs in order, gap seconds apart, stopping on 403 or 429."""
    results, stopped = [], None
    for n, url in enumerate(urls):
        if stopped:
            results.append((url, f"not checked, host answered {stopped} earlier", True))
            continue
        if n:
            time.sleep(gap)
        result = fetch(url)
        results.append(result)
        if result[1] in ("HTTP 403", "HTTP 429"):
            stopped = result[1]
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-net", action="store_true", help="skip the link check")
    ap.add_argument("--stale", type=int, default=60, help="days before a check counts as stale")
    ap.add_argument("--file", type=Path, default=DATA, help="data file (default: the real one)")
    ap.add_argument("--gap", type=float, default=3.0,
                    help="seconds between requests to the same host (minimum 3)")
    args = ap.parse_args()

    entries = yaml.safe_load(args.file.read_text()) or []
    today = dt.date.today()
    now_season = season(today)
    errors, warnings = [], []
    seen = {"id": {}, "title": {}, "url": {}}
    links: dict[str, list[str]] = {}  # url -> entries that use it
    verified_count = 0

    for i, e in enumerate(entries, 1):
        tag = f"[{i}] {e.get('id') or e.get('title') or 'no id'}"
        err = lambda msg: errors.append(f"{tag}: {msg}")
        warn = lambda msg: warnings.append(f"{tag}: {msg}")

        for k in e:
            if k not in KEYS:
                err(f"unknown key '{k}'")
        for k in REQUIRED_ALWAYS:
            if e.get(k) in (None, ""):
                err(f"missing '{k}'")

        if e.get("id") and not ID_RE.match(str(e["id"])):
            err(f"id '{e['id']}' is not a lowercase slug")
        if e.get("kind") is not None and e["kind"] not in KINDS:
            err(f"unknown kind '{e['kind']}'")
        if e.get("status") is not None and e["status"] not in STATUSES:
            err(f"unknown status '{e['status']}'")
        if e.get("applies_via") is not None and e["applies_via"] not in VIA:
            err(f"unknown applies_via '{e['applies_via']}'")
        for a in e.get("area") or []:
            if a not in AREAS:
                err(f"unknown area tag '{a}'")
        for k in FLAGS:
            if e.get(k) not in (True, False, None):
                err(f"'{k}' must be true, false or null, not '{e[k]}'")
        if e.get("usual_deadline") is not None and not USUAL_RE.match(str(e["usual_deadline"])):
            err(f"usual_deadline '{e['usual_deadline']}' should look like 'early February' or 'rolling'")

        try:
            deadline = as_date(e.get("deadline"))
            checked = as_date(e.get("last_verified"))
        except ValueError as exc:
            err(f"bad date ({exc})")
            deadline = checked = None

        if checked is None:
            warn("not verified yet, so it stays out of the CSV")
        else:
            verified_count += 1
            for k in REQUIRED_VERIFIED:
                if e.get(k) in (None, "", []):
                    err(f"verified but missing '{k}'")
            if deadline and not e.get("source_url"):
                err("verified deadline has no source_url")
            if (today - checked).days > args.stale:
                warn(f"last checked {checked}, over {args.stale} days ago")

        summer = e.get("summer")
        if isinstance(summer, int):
            if summer < now_season:
                warn(f"still on summer {summer}, the season is {now_season}")
            if deadline and deadline.year not in (summer - 1, summer):
                warn(f"deadline {deadline} is an odd year for summer {summer}")

        for key, store in seen.items():
            v = e.get(key)
            if v in store:
                (err if key == "id" else warn)(f"same {key} as entry {store[v]}")
            elif v:
                store[v] = i

        for k in URL_KEYS:
            if e.get(k):
                links.setdefault(e[k], []).append(f"{tag} {k}")

    if not args.no_net and links:
        by_host: dict[str, list[str]] = {}
        for url in links:
            by_host.setdefault(host_of(url), []).append(url)
        with ThreadPoolExecutor(max_workers=MAX_HOSTS_AT_ONCE) as pool:
            batches = pool.map(lambda urls: check_host(urls, max(args.gap, 3.0)), by_host.values())
            for url, problem, soft in (r for batch in batches for r in batch):
                if problem:
                    where = "; ".join(links[url])
                    msg = f"{where}: link {'refused a script' if soft else 'failed'}, {problem}: {url}"
                    (warnings if soft else errors).append(msg)

    print(f"{len(entries)} entries ({verified_count} verified), season {now_season}, "
          f"{len(links)} links{' (not checked)' if args.no_net else ''}, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    for line in errors:
        print("ERROR  ", line)
    for line in warnings:
        print("warn   ", line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
