# Candidate list (step 2)

Date: 2026-11-10. Names and links only. Deadlines, eligibility and flags are step 3.

**Saxon: the Include column is pre-filled with the lead's suggestion. Change any you disagree with,
and answer the rows marked `ask` with `in` or `out`.**

How the suggestions were made (2026-11-10): every row in the four main tables is `in`, since they are in
scope by definition. In Maybe, `in` covers solar and space physics, radio astronomy, planetary science,
the NASA Space Grant pointer, materials, condensed matter and optics sites, physics and astronomy
programs whose NSF award has ended or was not found (step 3 records whether they run in 2027, and
students search for them by name), and physics- or astronomy-specific programs run by universities,
societies or consortia outside NSF (SPS, LPI, KNAC, LA community college CURE, NDSU physics education).
Those last ones would carry Type `other`, a small widening of the "NSF, labs, NASA" scope. `ask` marks
programs open to all fields or not physics-specific (Caltech SURF and WAVE, Rutgers RISE, Wisconsin SROP,
DOE MLEF, AAPM medical physics, Princeton biophysics, RIT education research, Marshall math and physics).
`out` marks the one international program (ASTRON and JIVE), which waits for a later scope decision.

Sources used:

- NSF's REU site search (https://www.nsf.gov/funding/initiatives/reu/search) did not load. It returned an empty page to both automated tools, so it was not retried. In its place the NSF tables come from NSF's own award data (api.nsf.gov): active awards (ending on or after 2026-11-10) whose record says "REU Site", funded by the Physics (PHY) or Astronomical Sciences (AST) divisions. Three physics sites funded through Materials Research (DMR) are in the physics table because their names say physics. NSF's search filters by research area, not by funding division, so a few sites may sit under a different area there.
- Official lab, DOE and NASA pages.
- Juan's List, 2023 snapshot, as a checklist only. No text copied from it.
- Web search, only to find a program's own page. Every main page below was loaded on the program's own site unless the cell says "not loaded".

Key to "Found via": `NSF 1234567` is the NSF award number, `Juan 2023` means the program was on Juan's 2023 list, `search` means the page was found by web search and then loaded.

Counts: NSF REU (physics) 48, NSF REU (astronomy) 16, National labs 10, NASA 2, Maybe 46. Main tables 76. Needs a human 16. Not found or gone 21.

The five ids already in `programs.yml` are kept: `florida-astro`, `byu-physics`, `kentucky-physics` and `doe-suli` are in the main tables. `stonybrook-physics` is in Maybe, because no active NSF award was found for it (its award ended 2026-03-31).

## NSF REU (physics)

Count: 48

| Include | ID | Program | Host | Location | Main page | Found via |
|---|---|---|---|---|---|---|
| in | asu-cxfel | REU Site at the Compact X-ray Free Electron Laser (CXFEL) | Arizona State University | Tempe, AZ | https://biodesign.asu.edu/cxfel/get-involved/ | NSF 2447869, search |
| in | bhsu-underground | Multidisciplinary Underground Science at the Sanford Underground Research Facility | Black Hills State University | Spearfish, SD | https://www.bhsu.edu/university-resources/research/reu.html | NSF 2447788, Juan 2023 |
| in | byu-physics | Summer Research Programs at BYU | Brigham Young University | Provo, UT | https://reu.byu.edu/home | NSF 2348770, Juan 2023, also astronomy |
| in | queensborough-physics | Research Experiences for Community College Students in Physics and Astronomy | CUNY Queensborough Community College | Bayside, NY | https://www.qcc.cuny.edu/physics/reu.html | NSF 2548073, Juan 2023, also astronomy |
| in | caltech-ligo | LIGO SURF (Gravitational-Wave Science in the LIGO Project) | California Institute of Technology | Pasadena, CA | https://ligosurf.caltech.edu/ | NSF 2547402, Juan 2023 |
| in | catholic-physics | Physics Research in the Nation's Capital | The Catholic University of America | Washington, DC | https://sites.google.com/cua.edu/cua-physreu | NSF 2349155, Juan 2023 |
| in | coe-spectroscopy | Spectroscopy at Coe College (REU/RET) | Coe College | Cedar Rapids, IA | https://sites.google.com/a/coe.edu/coe-reu/ | NSF 2349118, Juan 2023 |
| in | columbia-nevis | Nevis Labs REU Program | Columbia University, Nevis Laboratories | Irvington, NY | https://www.nevis.columbia.edu/reu/ | NSF 2349438, Juan 2023. A second Nevis award (2608840) is based in Geneva, not checked |
| in | columbia-plasma | REU Site: Plasma Physics, Plasma Astrophysics, and Fusion | Columbia University | New York, NY | https://fusion.columbia.edu/reu-site (not loaded, 403) | NSF 2447137, search |
| in | duke-tunl | Undergraduate Research in Nuclear and Particle Physics at TUNL and Duke | Duke University | Durham, NC | https://tunl.duke.edu/education/reu | NSF 2547627, Juan 2023 |
| in | etamu-physics | Summer Research Program for Community College and Liberal Arts College Students | East Texas A&M University | Commerce, TX | https://www.etamu.edu/physics-and-autonomy/reu/ | NSF 2349111, search. The page title reads "Physics and Autonomy REU" |
| in | kstate-physics | Physics at Kansas State: Interactions of Matter, Light, and Learning | Kansas State University | Manhattan, KS | https://www.phys.ksu.edu/reu/ | NSF 2548403, Juan 2023 |
| in | lehigh-physics | Physics REU at Lehigh University | Lehigh University | Bethlehem, PA | https://physics.cas.lehigh.edu/undergraduate/reu-program | NSF 2446742, search |
| in | lsu-physics | Research in Physics and Astronomy at LSU | Louisiana State University | Baton Rouge, LA | https://www.lsu.edu/physics/undergraduate/research-experience.php | NSF 2447783, Juan 2023 (address changed) |
| in | msu-physics | REU in Physics at Michigan State | Michigan State University | East Lansing, MI | https://pa.msu.edu/academics/reu-program/ | NSF 2446884, Juan 2023 |
| in | ohiostate-physics | Summer Research Experience in Physics at Ohio State | The Ohio State University | Columbus, OH | https://physics.osu.edu/summer2026REU | NSF 2447734, search. The address names a year, so it may move |
| in | okstate-physics | Oklahoma State University Physics REU | Oklahoma State University | Stillwater, OK | https://physicsreu.okstate.edu/ | NSF 2349581, search |
| in | odu-accelerator | ODU/JLab REU in Accelerator and Nuclear Physics | Old Dominion University with Jefferson Lab | Norfolk, VA | https://www.jlab.org/accelerator/reu | NSF 2348822, Juan 2023 (old page shows 2018) |
| in | pennstate-physics | Sustainable Physics: From Subatomic to the Cosmos | Pennsylvania State University | University Park, PA | https://sites.psu.edu/physicsreu/ | NSF 2349159, search |
| in | purdue-physics | Multidisciplinary Physics at Purdue | Purdue University | West Lafayette, IN | https://www.physics.purdue.edu/research/reu/ | NSF 2244297, Juan 2023 |
| in | umich-paris-optics | Optics in the City of Light | University of Michigan | Paris, France | https://java.engin.umich.edu/ParisREU/ | NSF 2547056, Juan 2023 |
| in | umich-biophysics | Interdisciplinary Research Opportunities in Biophysics | University of Michigan | Ann Arbor, MI | https://lsa.umich.edu/biophysics/undergraduates/research-opportunities/reu-program.html (not loaded, 403) | NSF 2242779, Juan 2023 |
| in | tamu-cyclotron | Cyclotron Institute REU in Nuclear Science | Texas A&M University | College Station, TX | https://cyclotron.tamu.edu/reu | NSF 2447482, Juan 2023. Redirects to /reu-archive/, which carries the 2026 call |
| in | tcu-physics | Physics and Astrophysics at TCU | Texas Christian University | Fort Worth, TX | https://cse.tcu.edu/physics-astronomy/research/reu.php | NSF 2548326, Juan 2023, also astronomy |
| in | bu-physics | BU-PRO: Boston University Physics Research Opportunities | Boston University | Boston, MA | https://sites.bu.edu/physics-resources/physics-reu/ | NSF 2244795 (ends 2026-12-31, no renewal found), Juan 2023 |
| in | ucdavis-physics | UC Davis Physics REU | University of California, Davis | Davis, CA | https://london.ucdavis.edu/~zieve/REU/reu.html | NSF 2150515, Juan 2023 |
| in | ucsb-physics | Summer Research in Physics and Astronomy at UC Santa Barbara | University of California, Santa Barbara | Santa Barbara, CA | https://reu.physics.ucsb.edu/ | NSF 2349677, Juan 2023 |
| in | colorado-jila | Physics/JILA REU Program | University of Colorado Boulder | Boulder, CO | https://www.colorado.edu/physics-jila-reu/ | NSF 2548510, Juan 2023 |
| in | florida-gravity-ireu | International REU in Gravitational Physics | University of Florida | Several sites | https://ireu.phys.ufl.edu/ | NSF 2348913, Juan 2023 (old address 404). Research is abroad |
| in | illinois-physics | Physics REU at Illinois | University of Illinois Urbana-Champaign | Urbana, IL | https://physics.illinois.edu/research/reu | NSF 2244433, Juan 2023 |
| in | kansas-physics | KU Physics and Astronomy REU | University of Kansas | Lawrence, KS | https://physastroreu.ku.edu/ | NSF 2447841, Juan 2023 |
| in | kentucky-physics | Research in Symmetries (Physics and Astronomy REU) | University of Kentucky | Lexington, KY | https://pa.as.uky.edu/reu | NSF 2349261, Juan 2023 |
| in | miami-physics | REU in Physical Sciences | University of Miami | Coral Gables, FL | https://physics.as.miami.edu/undergraduate-program/current-students/reu-in-physics-sciences/index.html | NSF 2244126, search |
| in | minnesota-physics | Physics and Astronomy REU | University of Minnesota | Minneapolis, MN | https://cse.umn.edu/physics/reu-program | NSF 2348668, Juan 2023 |
| in | unm-physics | Physics and Astronomy REU | University of New Mexico | Albuquerque, NM | https://physics.unm.edu/undergraduate/reu-program.html | NSF 2349212, Juan 2023 (old address 404) |
| in | notredame-physics | Physics REU and RET Programs | University of Notre Dame | Notre Dame, IN | https://physics.nd.edu/research/reu-program/ | NSF 2050527, Juan 2023 |
| in | oklahoma-physics | Physics and Astronomy REU (REU/RET) | University of Oklahoma | Norman, OK | https://www.ou.edu/cas/physics-astronomy/students/undergraduate/research/reu | NSF 2548211, Juan 2023 (old address 404) |
| in | rochester-physics | REU in Physics, Astrophysics, and Optics | University of Rochester | Rochester, NY | https://www.pas.rochester.edu/undergraduate/reu/index.html | NSF 2446653, Juan 2023 |
| in | southcarolina-physics | Undergraduate Research in Physics | University of South Carolina | Columbia, SC | https://sc.edu/study/colleges_schools/artsandsciences/physics_and_astronomy/research/reu/ | NSF 2349326, search |
| in | utdallas-physics | REU in Theoretical and Experimental Physics | University of Texas at Dallas | Richardson, TX | none found | NSF 2348872. See Needs a human |
| in | toledo-physics | Physics and Astronomy REU | University of Toledo | Toledo, OH | https://www.utoledo.edu/nsm/physast/programs/reu/ | NSF 2349585, search |
| in | utah-physics | Physics and Astronomy REU | University of Utah | Salt Lake City, UT | https://www.physics.utah.edu/reu-opportunities/ | NSF 2349237, Juan 2023 (address changed) |
| in | virginiatech-neutrino | Neutrino Physics at Virginia Tech | Virginia Tech | Blacksburg, VA | https://www.phys.vt.edu/Undergraduate/REU.html | NSF 2149165, Juan 2023 |
| in | washingtonstate-physics | The Physics of Waves from the Nanoscale to the Cosmic Scale | Washington State University | Pullman, WA | https://physics.wsu.edu/overview-research/reu/ | NSF 2349426, Juan 2023 |
| in | washu-physics | Artificial Intelligence in Modern Physics Research | Washington University in St. Louis | St. Louis, MO | https://physics.washu.edu/reu | NSF 2547979, search |
| in | gatech-physics | Broadening Participation and Resiliency in Physics | Georgia Institute of Technology | Atlanta, GA | https://physicsreu.gatech.edu/ | NSF 2244423 (DMR), Juan 2023 |
| in | howard-physics | REU Site in Physics at Howard University | Howard University | Washington, DC | none found (Juan's page 404) | NSF 2349300 (DMR), Juan 2023. See Needs a human |
| in | arkansas-physics | Summer Research in Physics | University of Arkansas | Fayetteville, AR | https://physics.uark.edu/undergraduate/reu-program/ | NSF 2547774 (DMR), Juan 2023 |

## NSF REU (astronomy)

Count: 16

| Include | ID | Program | Host | Location | Main page | Found via |
|---|---|---|---|---|---|---|
| in | nrao-reu | NRAO/GBO Summer Student Research (REU) | National Radio Astronomy Observatory and Green Bank Observatory | Several sites | https://science.nrao.edu/opportunities/student-programs/summerstudents | NSF 2349110, Juan 2023 (old address 404). Link taken from NRAO's Student Programs page. Also an NSF facility |
| in | noirlab-chile | NOIRLab REU Chile | NSF NOIRLab (AURA) | La Serena, Chile | https://noirlab.edu/science/resources/REU-PIA/REU-Chile | NSF 2349023, search. Also an NSF facility |
| in | cornell-astro | Astrophysics and Planetary Science REU | Cornell University | Ithaca, NY | https://astro.cornell.edu/undergraduate-research | NSF 2244064, Juan 2023. Old address redirects to this general undergraduate research page |
| in | mariamitchell-astro | REU Internship in Astronomy | Maria Mitchell Association | Nantucket, MA | https://www.mariamitchell.org/reu-internship-in-astronomy | NSF 2349202, Juan 2023 |
| in | nau-astro | NAU Astro REU | Northern Arizona University | Flagstaff, AZ | https://in.nau.edu/astro-reu/ (not loaded, nau.edu gave 403) | NSF 2349774, Juan 2023 |
| in | northwestern-ciera | CIERA REU | Northwestern University | Evanston, IL | https://sites.northwestern.edu/cierareu/ | NSF 2446392, Juan 2023 |
| in | rit-multimessenger | REU in Multimessenger Astrophysics | Rochester Institute of Technology | Rochester, NY | https://www.rit.edu/ccrg/research-experience-undergraduates-multimessenger-astrophysics | NSF 2349530, Juan 2023 (old address 404), also physics |
| in | rutgers-physics | Rutgers Physics and Astronomy REU | Rutgers University | Piscataway, NJ | https://reu.astro.rutgers.edu/ | NSF 2050950, Juan 2023, also physics |
| in | seti-institute | Life in the Universe REU | SETI Institute | Mountain View, CA | https://www.seti.org/education/reu/ | NSF 2447895, Juan 2023 |
| in | berkeley-seti | Berkeley SETI Research Center REU | University of California, Berkeley | Berkeley, CA | http://seti.berkeley.edu/Internship.html | NSF 2547394, Juan 2023 |
| in | ucsc-lamat | Lamat Summer Research Program | University of California, Santa Cruz | Santa Cruz, CA | https://lamat.ucsc.edu/ | NSF 2447606, Juan 2023 (old address 410 Gone) |
| in | florida-astro | Computational and Data Intensive Astrophysics REU | University of Florida | Gainesville, FL | https://astro.ufl.edu/reu/ | NSF 2348547, Juan 2023 |
| in | hawaii-ifa | Institute for Astronomy REU | University of Hawaii | Honolulu, HI | https://student.ifa.hawaii.edu/reu/ | NSF 2548017, search |
| in | utexas-astro | UT Austin Astronomy NSF REU Program | University of Texas at Austin | Austin, TX | https://astronomy.utexas.edu/research/student-research-opportunities/ut-austin-astronomy-nsf-reu-program | NSF 2244278, Juan 2023 (address changed) |
| in | wisconsin-astro | Astronomy and Astrophysics REU | University of Wisconsin-Madison | Madison, WI | https://www.astro.wisc.edu/undergraduate-program/uw-madison-reu-program/ | NSF 2447323, search. Link taken from the department's REU application page |
| in | wvu-astro | Undergraduate Astrophysics Research in Appalachia | West Virginia University | Morgantown, WV | https://gwac.wvu.edu/reu (not loaded, 403) | NSF 2348764, Juan 2023 |

## National labs

Count: 10

| Include | ID | Program | Host | Location | Main page | Found via |
|---|---|---|---|---|---|---|
| in | doe-suli | Science Undergraduate Laboratory Internships (SULI) | U.S. Department of Energy national laboratories | Several sites | https://science.osti.gov/wdts/suli | DOE WDTS, Juan 2023. Juan's separate Fermilab SULI and PPPL SULI entries are part of this |
| in | doe-cci | Community College Internships (CCI) | U.S. Department of Energy national laboratories | Several sites | https://science.osti.gov/wdts/cci | DOE WDTS |
| in | fermilab-prism | Program for Research Innovation and STEM Mentorship (PRISM) | Fermi National Accelerator Laboratory | Batavia, IL | https://internships.fnal.gov/fermilab-program-for-research-innovation-and-stem-mentorship-prism/ | Fermilab undergraduate programs page |
| in | fermilab-qcipu | Quantum Computing Internship for Physics Undergrads (QCIPU) | Fermi National Accelerator Laboratory | Batavia, IL | https://internships.fnal.gov/quantum-computing-internship-for-physics-undergraduates-program/ | Fermilab undergraduate programs page |
| in | fermilab-uscms | U.S. CMS Undergraduate Internship | Fermi National Accelerator Laboratory | Batavia, IL | https://internships.fnal.gov/u-s-cms-undergraduate-internship/ | Fermilab undergraduate programs page. The same page also lists a computational science internship and an LBNF/DUNE far site internship, left out |
| in | lanl-undergrad | Undergraduate Student Internship Program | Los Alamos National Laboratory | Los Alamos, NM | https://www.lanl.gov/engage/collaboration/student-programs/undergrad | LANL student programs |
| in | llnl-internships | Student Internship Programs | Lawrence Livermore National Laboratory | Livermore, CA | https://www.llnl.gov/join-our-team/careers/student-internship-veteran-programs | LLNL careers. An umbrella page for many internships |
| in | llnl-summer-scholar | Summer Scholar Internship Program | Lawrence Livermore National Laboratory (laser, fusion and extreme matter facilities) | Livermore, CA | https://lmf.llnl.gov/education/summer-scholar-internship-program | search |
| in | nist-surf | Summer Undergraduate Research Fellowship (SURF) | National Institute of Standards and Technology | Several sites | https://www.nist.gov/surf | NIST |
| in | stsci-sasp | Space Astronomy Summer Program | Space Telescope Science Institute | Baltimore, MD | https://www.stsci.edu/opportunities/space-astronomy-summer-program | search |

NRAO and NOIRLab are in the astronomy table, since NSF funds them as REU sites.

## NASA

Count: 2

| Include | ID | Program | Host | Location | Main page | Found via |
|---|---|---|---|---|---|---|
| in | nasa-internships | NASA Internship Programs | NASA Office of STEM Engagement | Several sites | https://www.nasa.gov/learning-resources/internship-programs/ | intern.nasa.gov redirects here. Applications go through the NASA STEM Gateway, https://stemgateway.nasa.gov/public/s/explore-opportunities |
| in | jpl-sip | JPL Summer Internship Program | NASA Jet Propulsion Laboratory | Pasadena, CA | https://www.jpl.nasa.gov/edu/intern/apply/summer-internship-program/ (not loaded, 403) | search |

The other JPL programs and Space Grant are in Maybe.

## Maybe

Count: 46. Physics or astronomy next door: solar and space physics, planetary science, materials physics, optics, NSF sites whose award has ended, and programs that are not NSF REUs.

| Include | ID | Program | Host | Location | Main page | Found via |
|---|---|---|---|---|---|---|
| in | montanastate-solar | Space Physics and Solar Astrophysics REU | Montana State University | Bozeman, MT | http://solar.physics.montana.edu/reu/ | NSF 2244344 (GEO), Juan 2023. Solar |
| in | colorado-solar | Boulder Solar Alliance REU | University of Colorado Boulder (LASP) | Boulder, CO | https://lasp.colorado.edu/reu/ | NSF 2447549 (GEO), Juan 2023. Solar and space |
| in | cfa-solar | SAO/NSF Solar REU Program | Center for Astrophysics, Harvard and Smithsonian | Cambridge, MA | https://www.cfa.harvard.edu/opportunities/graduate-undergraduate-programs/heassp-solar-physics-reu-program | NSF 2548366 (GEO), Juan 2023. Solar |
| in | uah-heliophysics | Heliophysics REU | University of Alabama in Huntsville | Huntsville, AL | https://www.uah.edu/cspar/reu | NSF 2548506 (GEO), search. Solar and space |
| in | njit-spaceweather | REU in Solar, Terrestrial, and Space Weather Sciences | New Jersey Institute of Technology | Newark, NJ | https://spaceweather.njit.edu/reu | NSF 2050792 (GEO), search. Solar and space |
| in | berkeley-assure | Advancing Space Science through Undergraduate Research Experiences (ASSURE) | University of California, Berkeley, Space Sciences Laboratory | Berkeley, CA | https://www.ssl.berkeley.edu/assure/ | NSF 2548067 (GEO), Juan 2023. Space sciences. Some page text is from 2016 |
| in | umich-picasso | Program in Climate and Space Science Observation (PICASSO) | University of Michigan | Ann Arbor, MI | not checked (umich.edu gave 403) | NSF 2348598 (GEO). Space and climate |
| in | mit-haystack | Haystack Observatory REU | MIT Haystack Observatory | Westford, MA | https://www.haystack.mit.edu/haystack-public-outreach/research-experiences-for-undergraduates-reu/ | NSF 2243909 (GEO), Juan 2023. Radio astronomy and geoscience |
| in | amnh-astro | Earth and Planetary Science and Astrophysics REU | American Museum of Natural History | New York, NY | https://www.amnh.org/our-research/richard-gilder-graduate-school/academics-and-research/fellowship-and-grant-opportunities/undergraduate-fellowships (not loaded, 403) | NSF 2348998 (GEO), Juan 2023. Planetary and astrophysics |
| in | carnegie-epiic | Earth and Planetary Science Interdisciplinary Internships at Carnegie (EPIIC) | Carnegie Science, Earth and Planets Laboratory | Washington, DC | https://epl.carnegiescience.edu/epiic-reu (not loaded, timed out) | NSF 2244322 (GEO), search. Planetary |
| in | lpi-intern | LPI Summer Intern Program in Planetary Science | Lunar and Planetary Institute (USRA) | Houston, TX | https://www.lpi.usra.edu/lpiintern/ | Juan 2023. Planetary |
| in | jpl-surp-planetary | NASA Summer Undergraduate Program for Planetary Research | NASA Jet Propulsion Laboratory | not checked | https://www.jpl.nasa.gov/edu/intern/apply/nasa-summer-undergraduate-program-for-planetary-research (not loaded, jpl.nasa.gov gave 403) | search. Planetary |
| in | nasa-pggurp | NASA Planetary Geology and Geophysics Undergraduate Research Program | NASA Jet Propulsion Laboratory | not checked | https://www.jpl.nasa.gov/edu/intern/apply/nasa-planetary-geology-and-geophysics-undergraduate-research-program/ (not loaded, jpl.nasa.gov gave 403) | search. Planetary |
| in | nasa-space-grant | NASA Space Grant (state consortia, one row for all) | NASA | Several sites | https://www.nasa.gov/learning-resources/national-space-grant-college-and-fellowship-project/ | search. Each state consortium runs its own programs |
| in | maglab-reu | National MagLab REU | National High Magnetic Field Laboratory | Tallahassee, FL | https://nationalmaglab.org/education/college-students/reu | NSF 2128556 (DMR, part of the MagLab award), Juan 2023. Materials physics |
| in | georgetown-physics | Georgetown REU for Materials Physics | Georgetown University | Washington, DC | https://physics.georgetown.edu/reu/ | NSF 2349397 (DMR), Juan 2023. Materials physics |
| in | vcu-magnetics | REU Site in Magnetics | Virginia Commonwealth University | Richmond, VA | https://egr.vcu.edu/departments/mechanical-nuclear-engineering/magnetics-reu/ | NSF 2349694 (DMR), search. Materials physics |
| in | wooster-physics | Physics and Chemistry Research at the College of Wooster | The College of Wooster | Wooster, OH | https://physics.wooster.edu/reu/ (not loaded, connection failed) | NSF 2348889 (DMR), search |
| ask | marshall-amps | Appalachian Mathematics and Physics Site (AMPS) | Marshall University | Huntington, WV | https://amps.marshall.edu/ | NSF 2349289 (DMS), search. Mathematics and physics |
| in | ohiostate-cem | Center for Emergent Materials REU | The Ohio State University | Columbus, OH | https://cem.osu.edu/education-and-outreach/reu | Juan 2023. Materials |
| in | illinois-mrsec | Illinois MRSEC REU | University of Illinois Urbana-Champaign | Urbana, IL | https://mrsec.illinois.edu/reu-program | Juan 2023. Materials |
| in | colostate-lasers | REU in Ultraintense Lasers and High Field Photonics | Colorado State University | Fort Collins, CO | https://lasers.colostate.edu/research-experience-for-undergraduate-students/ | NSF 2447907 (ENG), search. Optics |
| in | ucf-creol | Unleashing the Light: Building the Future of Laser Technologies | University of Central Florida, CREOL | Orlando, FL | https://creol.ucf.edu/reu/ | NSF 2349439 (ENG), search. Optics |
| in | rochester-optics | Nanophotonics, Quantum Photonics, and Vision/Biomedical Optics REU | University of Rochester, Institute of Optics | Rochester, NY | https://hajim.rochester.edu/optics/undergraduate/reu.html | NSF 2244031 (ENG), search. Optics |
| in | stonybrook-physics | Physics and Astronomy REU at Stony Brook | Stony Brook University | Stony Brook, NY | https://www.stonybrook.edu/commcms/physics-reu/ | Juan 2023. NSF award 2243856 ended 2026-03-31, no active award found. Page loads |
| in | indiana-physics | Summer REU Program in Physics | Indiana University | Bloomington, IN | https://physics.indiana.edu/outreach/reu-program/index.html | Juan 2023. NSF award 2150234 ended 2025-04-30, no active award found. Page loads |
| in | cornell-classe | Accelerator Physics and Synchrotron Radiation Science REU | Cornell University, CLASSE | Ithaca, NY | https://www.classe.cornell.edu/StudentOpportunities/ReuProgram.html | Juan 2023. NSF award 2150125 ended 2026-02-28, no active award found. Page loads |
| in | umd-trend | TREND REU in Nonlinear Dynamics | University of Maryland | College Park, MD | https://trend.umd.edu | Juan 2023. NSF award 2150399 ended 2026-01-31, no active award found. Page loads |
| in | gsu-astro | REU in Astronomy and Physics | Georgia State University | Atlanta, GA | https://physics-astro.gsu.edu/reu/ | Juan 2023. No NSF award found. Page loads |
| in | cfa-astro | SAO Astronomy Summer Intern Program (Astro REU) | Center for Astrophysics, Harvard and Smithsonian | Cambridge, MA | https://www.cfa.harvard.edu/opportunities/graduate-undergraduate-programs/reu-summer-intern-program | Juan 2023. Page calls it an REU, no matching active NSF award found |
| in | knac-astro | Keck Northeast Astronomy Consortium | KNAC (member colleges) | Several sites | https://sites.google.com/wellesley.edu/knac/ | Juan 2023 (address changed). Recruits mostly from member colleges |
| in | cmu-physics | NSF REU in Physics | Carnegie Mellon University | Pittsburgh, PA | https://www.cmu.edu/physics/outreach/nsf-reu/index.html | search. No matching PHY REU Site award found |
| in | florida-physics | Physics REU | University of Florida | Gainesville, FL | https://phys.ufl.edu/undergraduate/reu-research-experiences-for-undergraduates/ | search. No active PHY REU Site award found apart from the international one |
| ask | caltech-surf | Summer Undergraduate Research Fellowships (SURF) | California Institute of Technology | Pasadena, CA | https://www.sfp.caltech.edu/undergraduate-research/programs/surf | Juan 2023. All fields |
| ask | caltech-wave | WAVE Fellows Program | California Institute of Technology | Pasadena, CA | https://sfp.caltech.edu/undergraduate-research/programs/wavefellows | Juan 2023. All fields |
| in | sps-internships | SPS Summer Internship Program | Society of Physics Students (AIP) | Several sites | https://students.aip.org/internships/program-details | Juan 2023 (old address redirects). Research, policy and outreach placements |
| out | astron-summer | ASTRON and JIVE Summer Research Programme | ASTRON, Netherlands Institute for Radio Astronomy | Netherlands | https://www.astron.nl/education/summer-research-programme/ | Juan 2023 (address changed). International |
| ask | rutgers-rise | Research Intensive Summer Experience (RISE) | Rutgers University, Aresty Research Center | New Brunswick, NJ | https://aresty.rutgers.edu/programs-funding/the-research-intensive-summer-experience | Juan 2023 (address changed). All fields |
| ask | wisc-srop | Summer Research Opportunity Program (SROP) | University of Wisconsin-Madison Graduate School | Madison, WI | https://grad.wisc.edu/explore/prepare/summer-research-opportunities/ | Juan 2023 (old address 404). Umbrella application that the UW-Madison astronomy REU uses |
| ask | doe-mlef | Mickey Leland Energy Fellowship (MLEF) | U.S. Department of Energy (run by ORISE) | Several sites | https://orise.orau.gov/mlef/ | Juan 2023. Energy, not physics specific |
| in | ndsu-per | Physics Education Research REU | North Dakota State University | Fargo, ND | https://www.ndsu.edu/dber/reu-program | Juan 2023 (address changed). Physics education |
| ask | rit-dber | Discipline-Based Education Research REU | Rochester Institute of Technology, CASTLE | Rochester, NY | https://www.rit.edu/castle/research-experience-undergraduates | Juan 2023 (address changed). STEM education |
| ask | aapm-summer | AAPM Summer Undergraduate Fellowship and DREAM Program | American Association of Physicists in Medicine | Several sites | https://www.aapm.org/education/GrantsFellowships.asp (not loaded, timed out) | Juan 2023. Medical physics |
| ask | princeton-biophysics | Summer Research in Molecular Biophysics REU | Princeton University | Princeton, NJ | https://reumolbiophysics.princeton.edu (not loaded, 403) | Juan 2023. Biophysics |
| in | lacc-cure | Consortium for Undergraduate Research Experiences (CURE) | Los Angeles City College | Los Angeles, CA | https://www.lacc.edu/academics/pathways/stem/physics-engineering-dept/cure (not loaded, 403) | Juan 2023 (address changed). Astronomy and planetary, LA-area community college students |
| in | ucmerced-physics | Physics REU at UC Merced | University of California, Merced | Merced, CA | https://physics.ucmerced.edu/PhysicsREU (not loaded, 403) | Juan 2023. NSF award 2150531 ended 2025-02-28 |

## Needs a human

Sites that refused automated reading or could not be read. Per the rule, a domain that answered 403 or 429 got no further requests. No retries after a 403.

| What | URL | What happened |
|---|---|---|
| NSF REU site search | https://www.nsf.gov/funding/initiatives/reu/search | Empty page (HTTP 202, no content) to curl and to the fetch tool. Not retried. NSF award data used instead |
| Columbia plasma REU | https://fusion.columbia.edu/reu-site | 403. columbia.edu then stopped, so the Geneva-based Nevis award (2608840) was not checked either |
| University of Michigan pages | https://lsa.umich.edu/biophysics/undergraduates/research-opportunities/reu-program.html | 403. umich.edu then stopped. Not requested: UM Physics REU (http://reu.physics.lsa.umich.edu/, NSF award ended 2026-04-30), UM CERN REU (http://cern-reu.physics.lsa.umich.edu, NSF award ended 2026-05-31), PICASSO (no URL found) |
| NAU Astro REU | http://www.physics.nau.edu/~reu/ | 403 on Juan's address. The current page found by search, https://in.nau.edu/astro-reu/, was not requested |
| WVU astrophysics REU | https://gwac.wvu.edu/reu | 403 |
| JPL programs | https://www.jpl.nasa.gov/edu/intern/apply/summer-internship-program/ | TLS error, then 403 to curl. jpl.nasa.gov then stopped (SIP, planetary SURP, PGGURP). www.nasa.gov is a separate host and answered normally |
| AMNH REU | https://www.amnh.org/our-research/richard-gilder-graduate-school/academics-and-research/fellowship-and-grant-opportunities/undergraduate-fellowships | 403 |
| APS/IBM Research Internship | https://www.aps.org/programs/women/scholarships/ibm/index.cfm | 403. Not in any table, so a human should check whether it still runs |
| LA City College CURE | https://www.lacc.edu/academics/pathways/stem/physics-engineering-dept/cure | 403 |
| UC Merced Physics REU | https://physics.ucmerced.edu/PhysicsREU | 403 |
| Princeton Molecular Biophysics REU | https://reumolbiophysics.princeton.edu | 403 |
| College of Wooster REU | https://physics.wooster.edu/reu/ | Connection failed in both tools (certificate problem) |
| Carnegie EPIIC | https://epl.carnegiescience.edu/epiic-reu | Timed out twice |
| AAPM fellowships | https://www.aapm.org/education/GrantsFellowships.asp | Timed out, then redirected to https://gaf.aapm.org/, which failed |
| Howard University Physics REU | https://physics.howard.edu/people/student-support/summer-internship-opportunities/reu | 404 on Juan's address. The NSF award is active (2349300), but no current page was found |
| UT Dallas Physics REU | none found | NSF award active (2348872). Search found only news items, and the physics department site failed a certificate check |

## Out of scope (from Juan's 2023 list)

- AAAS Mass Media Science and Engineering Fellows Program
- Amgen Scholars Program
- Summer Program for Undergraduate Research at the Medical College of Wisconsin
- REU Program in Advanced Technologies for the Preservation of Biological Systems (ATP-Bio)
- REU Program for Energy and the Environment at the University of Minnesota
- Summer Undergraduate Research Experience (SURE) at the USC Viterbi School of Engineering
- Lloyd V. Berkner Space Policy Internships
- Minnesota High Tech Association SciTechsperience Internship
- Smithsonian Institution Hosted Internships (a list of lists)
- American Mathematical Society REU Links (a list of lists)

## Not found or gone

| Program | Juan's or last known URL | What we saw |
|---|---|---|
| Vanderbilt REU in Physics and Astronomy | http://www.vanderbilt.edu/AnS/physics/reu/ | 404. NSF award 2149863 ended 2025-02-28 |
| University of Wyoming Astronomy REU | http://www.uwyo.edu/physics/reu-info/index.html | Server error 500. NSF award 2244317 ended 2026-03-31 |
| University of Nebraska Lasers and Optics REU | https://www.unl.edu/summerprogram/reu-augmented-reality-and-physics | 404. NSF award 2051059 ended 2025-02-28 |
| UTRGV REU and RET Site in Physics | http://www.utrgv.edu/reu | Redirects to the department home page. NSF award 2244167 ended 2026-09-30 |
| University of Chicago Physics REU | https://physics.uchicago.edu/research-experiences-for-undergraduates/ | Page says the Physics REU will not run Summer 2026. NSF award 2051126 ended 2026-02-28 |
| University of Washington Physics and Astronomy REU | https://sites.google.com/uw.edu/uwreu | Page lists Summer 2026 as canceled. NSF award 2243362 ended 2026-03-31 |
| Montana State Quantum and Materials Physics REU | https://physics.montana.edu/reu.html | Page says the program was not offered in summer 2024 |
| Arecibo Observatory REU | https://www.naic.edu/REUT/ | Certificate name mismatch, no page. NSF award 2149880 (Universidad Metropolitana) ended 2026-03-31 |
| Numentus Technologies REU | http://numentus.net/students/ | Page now lists company services, no REU. NSF award 2205624 ended 2026-06-30 |
| USF Applied Physics REU | https://www.usf.edu/arts-sciences/departments/physics/ap-reu/ | 404 |
| UW-River Falls Neutrino Astrophysics | https://www.uwrf.edu/PHYS/Internships-REU-and-Astrophysics.cfm | 404 |
| Miami University (Ohio) Physics REU | http://miamioh.edu/cas/academics/departments/physics/academics/reu-program/index.html | Redirects to the department home page |
| Fermilab SIST | https://internships.fnal.gov/summer-internships-in-science-and-technology-sist/ | 404, and not on Fermilab's current undergraduate programs page |
| National Solar Observatory REU | http://eo.nso.edu/REU | 404. No separate NSO page found |
| DHS HS-STEM Summer Internships | https://orise.orau.gov/dhseducation/hs-power/default.html | Redirects to an ORISE "page not found" page |
| Cornell Center for Materials Research REU | https://www.ccmr.cornell.edu/education/graduate-and-undergraduate-programs/ | 404 |
| Northwestern MRSEC undergraduate program | https://mrsec.northwestern.edu/undergraduate-opportunities/ | 404 |
| University of Chicago MRSEC REU | https://mrsec.uchicago.edu/reu/ | 404 |
| Vanderbilt VINSE REU | https://www.vanderbilt.edu/vinse/reu/ | Redirects to a 2020 news post |
| Mississippi State computational materials REU | https://www.ccs.msstate.edu/conferences/REU2022/ | Page covers 2022 only |
| Rice Planetary Habitability REU | https://earthscience.rice.edu/academics/2022-nsf-reu/ | Host name no longer resolves |
