# Opportunities: brainstorm (2026-11-06)

Not rendered (underscore folder). Merged from the lead session's ideas and the advisor's, each written
without seeing the other. Saxon is still deciding; nothing here is settled.

## The three problems (Saxon's, from applying himself)

1. Program and application information is buried somewhere different on every department site.
2. Keeping track of applications and deadlines across many programs is hard.
3. The pieces of an application, and the program information, are hard to understand.

## Facts checked by the advisor on 2026-11-06

- NSF REU solicitation 23-601: participants must be U.S. citizens, nationals or permanent residents.
  "Undergraduate" includes students working toward an associate degree, so community college students
  qualify by rule. A student who has finished the bachelor's and is no longer enrolled is not eligible,
  which is why most sites exclude May graduates (a few allow them). Stipend about $700 a week. At least
  half of a site's participants must come from institutions with limited research.
- ETAP: NSF's common application. One profile reused across sites, saved statements, transcript and CV,
  a keyword search of opportunities, a "My References" area with references chosen per application,
  email when a letter arrives, status tracking. NOT confirmed: whether one uploaded letter serves every
  application. Walk through it before writing anything about it.
- Usual pieces for physics and astronomy sites: CV, a personal statement or statement of interest,
  unofficial transcript, two letters (a few ask one, some allow three), a course list. No test scores.
- Timing: astronomy sites agree on no offers before March 1. Physics sites share an accept-or-decline
  date about a week later (March 8 in 2024), which moves each year.
- Not yet checked: that stipends are taxable with no withholding.

## Where the two views differed

The lead wanted a full same-shape card per program (money, every application piece, statement prompts)
to fix problem 1. The advisor said never store those facts: they change every year and a stale row
misleads more than a missing one. Synthesis: normalize where things are, not what they say. Store three
deep links per program (apply page, eligibility or FAQ page, project and mentor list), which the link
checker can test, plus a few slow-changing flags. Explain the common facts (NSF stipend, the eligibility
rule) once on an evergreen page instead of per program.

## Site map sketch

```
Opportunities            front door: "where are you?" picker (reuses the Lab Help wizard)
  Is an REU for me?      paid, housing, no experience needed, who they are for
  Find programs          the list: flags, deep links, last checked, .ics per deadline
  Build your application
    Decode a program page    one typical page, phrase by phrase, hover definitions
    The pieces               statement, letters, transcript, CV, course list
    An annotated application Saxon's 2022 statement with margin notes (his call)
    Glossary
  Track your applications  spreadsheet template and the letter-request kit; browser tracker later
  The season, month by month   October to April, this month highlighted
  After the deadline     offers, waitlists, reply date, no offer, cancelled after an offer
  For mentors and SPS officers   printable one-page handout
```

## Per-program entry (tiers by upkeep)

- Rarely changes, check every few years: name, host, area tags, kind, applies via (ETAP or own form),
  usual deadline month ("early February", so the page is useful in a year nobody checked), open to
  non-citizens, open to first and second years, open to community college students.
- Check every season (agents can do it): exact deadline, running or not, three deep links, last checked.
- Never store, link instead: stipend beyond the NSF norm, housing, letter count, statement prompts,
  project lists.
- A "report a correction" link on every entry, so programs and students fix rows.

## Tracker

- First: a spreadsheet template (Google Sheets "make a copy" and an .xlsx): program, portal, deadline,
  status, reply-by date, and a grid of letter writers by program with asked, confirmed and received dates.
- A letter-request kit: an example email to a professor, a one-page summary to send them, and a table
  of programs, portals and deadlines for each writer. Letters are the part students lose control of.
- A calendar file (.ics) per deadline from the list page. Cheap, no data kept.
- Later, only if the first two get used: an in-browser tracker (localStorage). Risks: a cleared cache
  loses it, it does not follow the student between phone and laptop, and on a shared computer the next
  person sees letter writers' names. If built: export and import, a visible "clear my data" button, never
  store statement text.

## Explanation (problem 3)

- Hover or tap definitions for: REU, ETAP, stipend, rising junior, citizen or permanent resident,
  "must not have graduated", statement of interest vs personal statement, unofficial transcript, letter
  portal, first offers, common reply date, waitlist, SULI, IREU, Space Grant.
- FAQ of misconceptions: no research experience is the point, not a barrier. GPA is read in context. A
  letter from a lab instructor who knows you beats a famous name. Apply to 8 to 12, not 2. Do not accept
  and then back out. Community college students are eligible for NSF sites.

## Accessibility (WCAG 2.2 AA, concrete)

- Filters are checkboxes in a fieldset with a legend. A polite live region says "12 programs shown".
- Status in words, never colour alone. Dates in `<time datetime>` and written out. Deadlines say "end of
  day in the program's time zone, check their page".
- The in-browser regrouping must not move keyboard focus.
- Targets at least 24 px (the AA minimum), 44 px where it fits on phones. One column on phones, no
  sticky filter bar on small screens.
- Native `<details>` for expandable entries, real buttons with visible labels, works without JavaScript,
  a print style for the list and the handout.

## Not to build (or not yet)

Per-program stipend and prompt fields, a scraper, a catalogue of every field (ETAP and NSF search do
that), international programs with visa guidance, notifications, comments or ratings, analytics, accounts.

## Rough priority by value per hour of Saxon's time

1. Decoder, glossary, timeline and FAQ (evergreen).
2. Spreadsheet tracker and letter-request kit.
3. Thin list with deep links, flags and .ics.
4. Front door picker.
5. Annotated application (only if he wants to publish his statement).
6. After-the-deadline page and the mentor handout.
7. Later: in-browser tracker, correction form, monthly link-check Action, grad school.

## Changes the draft would need if this direction holds

`programs.yml`: add `apply_url`, `eligibility_url`, `projects_url`, `usual_deadline`, and flags
`noncitizens_ok`, `first_second_year_ok`, `community_college_ok`. Drop `stipend`. `_reu.ejs`: show the
three links and the flags, fall back to `usual_deadline` when no exact date is posted, add a correction link.

## Open questions for Saxon

- Publish his 2022 Michigan statement, annotated?
- Spreadsheet first, browser tracker later: right order? Google Sheets, Excel, or both?
- Non-citizens: a flag on each program only, or also a short page of where else to look?
- How far "internships" reaches: national labs and NASA surely. Industry?
- Which words and steps confused him most in 2021 and 2022. He is the best source for the decoder;
  a 20-minute interview would cover it.

## Saxon's decisions (2026-11-06, after reading the above)

- Direct links approach: store where things are (apply, eligibility, projects), not what they say.
- Spreadsheet first, so a usable reference exists as soon as possible. In-browser tracker later, if at all.
- Non-citizens: a tag on each program is enough for now.
- Scope: physics and astronomy NSF REUs, plus national labs and NASA. Keep the schema open to more kinds.
- Decoder later. Saxon will write down what confused him and ask others about their experiences.
- Statements: maybe later, after his own review.
- Data before page and UX changes, so the design can be judged against real entries.
