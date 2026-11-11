# Opportunities: the plan

For any session picking this up. Read this file first, then `brainstorm.md` beside it for the reasons
behind the direction. The schema itself lives in the header of `opportunities/reu/programs.yml`, which
wins if this file and it ever disagree. Update the status line at every step boundary.

**Status (2026-11-11):** Steps 1 and 2 done. Saxon answered the `ask` rows and captured blocked pages by
hand (`saxon_investigation.md`, facts in `findings.md`, raw captures in the git-ignored `sources/`).
`candidates.md` now has 135 rows marked `in` and 2 small `ask`s. `columbia-plasma` is the first verified
entry in `programs.yml`. Next: agree how to run step 3 with Saxon, then run it.

## Goal

A free resource on saxonstockton.com that helps undergraduates find physics and astronomy summer research
programs and build their applications. It grew out of Juan Cabanela's list (MSU Moorhead, last updated
2023-02-23, gone by July 2024; last good copy at
https://web.archive.org/web/20230927051031/http://jupyter.mnstate.edu/reulist/) but is not a copy of it.
Saxon's three problems from applying himself: program and application information buried on department
sites, tracking applications and deadlines, and understanding what programs ask for.

## Decided (do not re-decide without Saxon)

Saxon, 2026-11-06:

- Direct links approach: store where things are (apply, eligibility, projects pages), not what they say.
- Spreadsheet first, so students have a usable reference as soon as possible.
- Non-citizens: a tag on each program, nothing more for now.
- Scope: physics and astronomy NSF REUs, national labs, NASA. The schema stays open to more kinds.
- Data before page and UX changes.
- Decoder and explanation pages later. Saxon collects notes on confusing parts and asks others.
- His old statements: private until he has reviewed them. Never put them in this public repo for review.

Lead and advisor, at Saxon's request, 2026-11-10:

- One workbook that is both the reference and the tracker, in Google Sheets only (no separate .xlsx).
- `programs.yml` is the only source. A script writes `data/summer-programs.csv`, which is committed and
  published on the site. The Sheet's Programs tab reads it with IMPORTDATA, so the master and every
  student copy stay current. The CSV is never edited by hand. It is not built in CI, so a data problem
  can never block a Lab Help deploy. `check_programs.py` will fail if the committed CSV is out of date.
- Entries with `last_verified: null` never reach the CSV.
- The CSV URL is `https://saxonstockton.com/data/summer-programs.csv`, outside `/opportunities/` because
  that folder name is still a working title and this URL is permanent.
- Permanent once published: the CSV URL, the CSV header names (new columns are only appended), and every
  `id`. Students' sheets look programs up by id and by header text, never by row or column position.
- Letters are tracked as a grid inside "My applications", not a separate long table.
- Formulas use INDEX/MATCH, not XLOOKUP, so a downloaded Excel copy still works.

## Rules that hold everywhere

- `last_verified` means every season field was re-read on the program's own pages that day. A search
  result or an aggregator is never a source.
- Unknown is null. Never guess a deadline, a flag or a link.
- Never flood a domain (Saxon, 2026-11-10). Every script and every agent that fetches pages sends at
  most one request every 3 seconds to any one domain, never two at once to the same domain, identifies
  itself as the saxonstockton.com link check, and stops asking a domain that answers 403 or 429 (that
  page goes to "needs a human", no retries). Parallel agents are split by domain, so two agents never work
  the same domain at once. `check_programs.py` enforces this in code (`--gap`, 3 seconds minimum).
- Never store stipend, housing, letter count or statement prompts. Link to the program.
- Notes are one factual line in our own words. Never copy Juan's descriptions or anyone else's.
- At the August 1 rollover: bump `summer`, clear `deadline`, `season_note` and `source_url`. Remove an
  entry only then, never mid-season.
- Nothing is committed, pushed, published or shared without Saxon's go-ahead. Every page under
  `opportunities/` stays `draft: true` until he says to publish (see `opportunities/_metadata.yml`).
- Anything written in his name (page text, the How to use tab) follows `~/TCU/voice-card.md` and is
  scaffolding for him to rewrite. Run `python collab/voice_check.py <file> --tells` from `~/TCU`.

## Steps

### 1. Fields (done 2026-11-10, waiting on Saxon's review)

Schema in the header of `opportunities/reu/programs.yml`. Five seed rows migrated, all unverified.
`scripts/check_programs.py` rewritten: unknown keys, id slugs and duplicates, vocabularies, true/false/null
flags, date and usual-deadline forms, required fields on verified rows, source_url with a deadline, all
five link fields (403 and 429 are warnings), `--file` for testing. `_reu.ejs` updated for `season_note` and
`location`. Page and UX work is step 6, not here.

### 2. Candidate list (one agent, then Saxon)

Gather names only, no details: physics and astronomy sites on NSF's REU search
(https://www.nsf.gov/funding/initiatives/reu/search), national lab programs (DOE SULI and the labs' own
undergraduate programs), NASA internships (the NASA Gateway and center programs such as JPL), and the
non-NSF programs in Juan's 2023 copy above. Output: `opportunities/_notes/candidates.md`, a table per
kind with name, host, main page URL and a proposed id, plus counts. Saxon marks what is in or out before
step 3. Expect 60 to 90.

### 3. Verify (agents in parallel, then a second agent, then the checker)

- Batches of about 10 candidates per agent, grouped by domain: every program on one domain goes to the
  same agent, so no two agents hit a domain at once. Each agent's brief repeats the rate rule above.
- Each agent gets its batch, the schema header of
  `programs.yml`, and these rules: read only the program's own pages (and official portals: ETAP, the
  NASA Gateway, DOE WDTS); fill what the pages state; null what they do not; set `last_verified` to the
  day read and `source_url` wherever a deadline came from; `note` in its own words or null.
- Sites that refuse automated reading go on a "needs a human" list in `candidates.md`, never guessed.
- A different agent re-checks a sample of about 15 percent against the pages. Nobody signs off their
  own batch.
- The lead merges the batches into `programs.yml` and runs the checker until it shows 0 errors.

### 3b. The watcher (right after step 3, added 2026-11-10)

Catches programs posting or changing their details during the season, without re-verifying everything.
Most valuable November to February, so it is built before the workbook, not after publication.

- `scripts/watch_programs.py`, no AI: for each entry, fetch `url`, `apply_url`, `eligibility_url` and
  `source_url` (each URL once), keep only the lines that matter (dates, the words deadline, apply,
  eligibility, citizen, the season year), and compare with last week's copy. Report pages whose lines
  changed, and flag "now mentions <season>" for entries with no deadline yet.
- Last week's copies live on a separate `watch-state` branch, never on `main` (every push to `main`
  redeploys the site).
- `.github/workflows/watch-programs.yml`: weekly schedule plus a manual button. Runs the script, opens or
  updates one GitHub issue listing the changes, never touches `main`. GitHub pauses scheduled workflows
  after 60 days without repository activity, so a quiet summer can stop it.
- Then an agent re-reads only the flagged pages and proposes edits to `programs.yml`. The lead merges
  them once the checker shows 0 errors, and Saxon sees the list of changes.
- Blind spots: pages that refuse scripts or are built in JavaScript (ETAP) cannot be watched. They stay on
  the "needs a human" list in `candidates.md`.
- Polite by design: weekly, one request per page, the same per-domain spacing and 403/429 stop as the
  checker (reuse its `check_host`), and it honours each domain's robots.txt, including any Crawl-delay
  longer than 3 seconds. A page robots.txt disallows goes to "needs a human" instead of being fetched.
- The same signal feeds a "recently updated" banner on the list page in step 6.

### 4. Saxon's review (about 30 minutes)

He spot-checks about 10 entries and clears the "needs a human" list.

### 5. The workbook

1. `scripts/build_programs_csv.py`: a pure function of the YAML. Verified rows only, sorted by id, headers
   in the schema order, flags printed Yes / No / Not stated, area joined with ", ". Add the out-of-date
   check to `check_programs.py`. Add `data/summer-programs.csv` to `project.resources` in `_quarto.yml`.
2. Build the workbook locally as .xlsx (`openpyxl` is not in `.venv` yet). Tabs:
   - Programs: `=IFERROR(IMPORTDATA(Settings!B1), Snapshot!A:Z)`.
   - My applications: 25 pre-filled rows, per-row formulas (no ARRAYFORMULA), edits warned not blocked.
     Columns: Program (dropdown of ids, warn but accept anything typed) | Deadline (looked up, can be
     typed over) | Days left | Status (Considering, Working on it, Submitted, Offer, Waitlisted, Not
     offered, Accepted, Declined) | three letter columns headed by writer names, each blank, Needed,
     Requested or Received | Apply link | Apply through | Reply by | Notes | Program name.
   - Letter writers: name, email, asked on, said yes on, sent my list on, thanked.
   - How to use: short, in Saxon's name, scaffolding for him to rewrite.
   - Snapshot (hidden): a static copy of the CSV, the fallback when IMPORTDATA has not been allowed.
   - Settings (hidden): B1 holds the CSV URL, so a student can repair it.
   - A template version number somewhere visible.
3. Answered by Saxon on 2026-11-10: yes, commit `opportunities/`, `scripts/` and `data/` to the public
   repo and publish the CSV of verified rows while the pages stay draft. The Drive connector's Google
   account is his personal one and stays active after TCU, so the master lives there. Yes, share the
   master view-only by link (it guards the master against accidental edits).
4. Push, confirm the CSV URL returns 200, then upload the .xlsx through the Drive connector with
   conversion to a Google Sheet. The conversion may drop the formula or the protection; fix by hand once.
5. **Saxon:** in a desktop browser, open the master and click "Allow access" for IMPORTDATA (the phone
   app cannot). Then make a copy on his phone and confirm the snapshot shows and the dropdown works.
   IMPORTDATA consent is per spreadsheet and editors only, so every student copy needs the same click.
   If the IFERROR fallback misbehaves, use a bare IMPORTDATA and make "open once on a computer and click
   Allow access" step 1 of How to use.
6. Share the master view-only, and link its `/copy` URL from one place on the site.

### 6. Pages and UX, with the real data

The list shows the three links and the flags, falls back to `usual_deadline`, gets filters (checkboxes in
a fieldset, a live region for the count), a calendar file per deadline and a "report a correction" link
per entry. The hub links to the workbook, and the placeholder text is rewritten. Accessibility notes in
`brainstorm.md`. Screenshots for Saxon, then the voice scan.

### 7. Publish (Saxon's go-ahead)

Remove `draft: true`, uncomment every `OPPORTUNITIES DRAFT` entry, commit, push, check the Actions run and
the live pages. Then share with SPS chapters, the TCU physics undergraduates and other contacts.

## Adding a field later

1. Add the key to the schema in `programs.yml` and to `KEYS` in `check_programs.py`.
2. Append its column to the end of the CSV, never in the middle, so students' sheets keep working.
3. Backfill it with one agent pass that starts from each entry's stored links.
4. Decide whether it changes yearly. If it does, add it to the seasonal check and the August rollover.
   If it does not, check it every few years. Stipend, housing, letter count and prompts are on the
   never-store list by decision, not by limitation: adding one means Saxon reverses that decision.

## Later, not in this plan

The decoder, glossary, timeline and FAQ. Annotated statements (Saxon's call, after his private review).
An after-the-deadline page. A mentor handout. More kinds (industry, international). A monthly link-check
Action. Graduate school pages in `opportunities/grad-school/`.

## Files

| Path | What |
|---|---|
| `opportunities/_notes/plan.md` | this plan |
| `opportunities/_notes/brainstorm.md` | the ideas, the reasons, Saxon's decisions |
| `opportunities/reu/programs.yml` | the list and its schema |
| `opportunities/reu/_reu.ejs`, `index.qmd` | the list page (three listings, browser regrouping) |
| `scripts/check_programs.py` | the checker |
| `opportunities/_metadata.yml` | the draft switch |
| `scripts/build_programs_csv.py`, `data/summer-programs.csv` | step 5, not written yet |
