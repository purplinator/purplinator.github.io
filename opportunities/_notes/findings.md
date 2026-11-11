# Findings from Saxon's manual captures

Facts taken from pages Saxon read and captured by hand on 2026-11-11, in our own words. The raw captures
are in `sources/`, which git ignores (other sites' page text, and NSF exports with contact details). His
own notes and decisions are in `saxon_investigation.md`. Step 3 agents read this file as hints and
confirm against the live page wherever the page can be loaded.

## What blocks automated reading

- NSF's REU site search asks bots to stay away and sits behind a firewall that refuses headless browsers.
  Saxon exported it by hand twice: physics and astronomy sites (74 rows, 62 distinct awards) and all
  sites (480 rows). Its records often carry an older award number than NSF's award data, so programs are
  matched by institution and website, not by award number. Its "Site Website" column is the best single
  source for program URLs, and one site points straight at its ETAP opportunity page.
- The AAS "Internships and Summer Jobs" page and several university sites (see "Needs a human" in
  `candidates.md`) also refuse automated browsers. Manual capture works.

## Program facts

### Columbia plasma REU (`columbia-plasma`)

Read 2026-11-11 on https://fusion.columbia.edu/reu-site (NSF's export lists it under
plasma.apam.columbia.edu, which is the same site). Entered in `programs.yml` as verified.

- Applications for Summer 2027 are open, due January 31, 2027, through two Google Forms: a main
  application and a separate form for letters of recommendation.
- Program dates: June 1 to August 6, 2027, ten weeks.
- U.S. citizens or permanent residents only. Must be enrolled in an undergraduate degree in physics or a
  related engineering field and not yet graduated. Must be 18 or older.
- Aimed at students from outside Columbia. Students from colleges with little research, and students from
  underrepresented groups, are encouraged to apply.
- The program includes travel support to a professional meeting. (Stipend amount is on the page but is
  never stored, per the plan.)

### AAPM medical physics programs (`aapm-sfp`, `aapm-dream`)

From AAPM's fellowships index page, captured 2026-11-11. The exact page address was not recorded, so the
deadlines below still need a `source_url` from step 3 before they count as verified.

- Summer Undergraduate Fellowship Program (2027): student applications due February 9, 2027, 11:59 pm
  Eastern. Decisions by March 3, 2027. Mentor matching March 22 to 26, 2027.
- DREAM (2027): same student deadline, decision date and matching week.
- Each program has its own page on AAPM's application platform (the links in `candidates.md`).
- AAPM's other listings are graduate, travel or early career awards, not undergraduate summer programs.

### Marshall (`marshall-mathphysics`)

The math and physics REU now lives at https://mathphysicsreu.marshall.edu. The old AMPS site,
https://amps.marshall.edu, is for the program that is ending.

### Caltech SURF and WAVE (`caltech-surf`, `caltech-wave`)

SURF works differently from a site REU. Mentors post individual project listings, much like job
openings, and each listing carries its own timeline, eligibility and project details. The list entry
should point at those listings rather than promise one deadline. WAVE has its own structure, which is less
clear. Saxon thinks it is more flexible and may not follow a fixed cycle. Step 3 should describe both from
their pages.

### Rutgers RISE (`rutgers-rise`)

Applications open in the spring. Keep it on the list with no deadline until the date is posted.

### NAU (`nau-astro`)

Current page: https://in.nau.edu/astro-reu/ (Juan's old address is dead).

### University of Michigan (`umich-physics`, `umich-cern`, `umich-biophysics`, `umich-paris-optics`)

umich.edu refuses automated reading, and two of these NSF awards have ended. Saxon has contacts there and
can ask directly if step 3 cannot settle whether they run in 2027.

## Saxon's scope calls (2026-11-11)

- Keep broad programs that match students with advisors (Wisconsin SROP), specialized ones (DOE Mickey
  Leland, AAPM medical physics, Princeton biophysics, RIT education research) and spring-cycle ones
  (Rutgers RISE). The aim is to encourage students to explore.
- Programs not meant for undergraduates (ASTRON and JIVE) wait for a later list, in "For later" in
  `candidates.md`.
