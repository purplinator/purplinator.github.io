# Lab report format: reference notes

Source of truth for the Lab Help pages about how a lab is turned in. Written down from
Saxon's description on 2026-10-11, plus what the Lab 4 and Lab 5 templates in `files/`
show. Quarto does not render anything in an underscore folder, so this file is notes only.
Facts first; suggestions and the page plan are kept separate at the end.

## Setting

- Intro physics lab (TCU "P1"), groups of three (sometimes two). Each student takes one job for
  the lab: **QPD** (Question, Procedure, Diagram), **UDA** (Uncertainty, Data, Analysis) or
  **CON** (Conclusion). Every lab has the three parts. Lab 9 additionally opens with a theory
  / pre-QPD session that takes the whole first class period; the three-part lab is the second.
- Each job writes on its own personal whiteboard, roughly 0.75 m by 0.5 m (landscape, 3:2).
  The board is photographed and the photo pasted into that lab's Word report template.
- Report template (one `.docx` per lab): name, partners, section; then one table per job
  with placeholder text saying which images go where.
  - QPD table: photo of the QPD board; annotated photo of the physical setup (text boxes
    and arrows labelling the measurable quantities); where the lab uses a sensor, a
    screenshot of the sensor graph with the recorded values highlighted.
  - UDA table: screenshot of the completed data table *with the uncertainty rows filled
    in*; screenshot of the graph with every data set and every best-fit function; photo of
    the UDA board (derivation and sample calculations).
  - CON table: photo of the CON board.
- Submission policy (confirmed 2026-10-11): regular labs, each student turns in only the part
  they worked on; in a group of two, one does QPD, one does UDA, both write CON and each turns
  in their part plus CON. Major labs (5 and 9): every student turns in every part, and the
  grade depends on the partners' work too.
- Excel analysis template (one `.xlsx` per lab): yellow cells are raw data to type in,
  light blue cells are equations to enter, row 35 is the mean, row 36 `abs unc, δa`, row 37
  `rel unc, δr`. Lab 4's sheet has no highlighting at all. The uncertainty page covers how
  to fill those rows.

## Rules that apply to every job

- Header at the top of the board: the student's name and the job label (QPD, UDA or CON).
- Units on every number, every variable definition, every axis. This is the most common
  thing students forget and the most common deduction.
- The conclusion is written as a paragraph, not as a list of answers.

## QPD: Question, Procedure, Diagram

1. **Header** (name, "QPD") at the top.
2. **Question**, written as a title directly under the header. It always has the form
   "What is the relationship between *x* and *y*?", where *x* and *y* are the physical
   quantities in words, not letters: "the height of the launcher and the distance the ball
   bearing travels", not "*h* and *d*".
3. **Procedure**, taking most of the board. Step-by-step, written so that someone who knows
   nothing about the lab could do it, and stating exactly which variables are measured and
   recorded and in what units.
4. **Annotated diagram.** Usually a photo of the setup annotated in Word with arrows and
   labels for the measurable quantities (positions, distances, angles). Some students draw
   the diagram instead, on a split board or a second board, either in place of the photo or
   as well as it.

## UDA: Uncertainty, Data, Analysis

Most of this job happens in Excel, not on the board:

- Enter the data, complete every calculated column, fill both uncertainty rows for every
  column, make the graphs.
- Nearly every lab ends with a linearized graph carrying a trendline with its equation
  displayed, even when the relationship under test is not linear. When the relationship is
  linear, the relationship graph and the linearized graph are the same graph.

On the board:

1. **Header** (name, "UDA").
2. **Derivation** of the setup mathematics: whatever gets from the physics to the quantity
   being graphed. Sometimes a free-body diagram followed by the force equations and the
   resulting relationship; sometimes a shorter derivation.
3. **Sample calculation for every calculated column** in the sheet. Pick a real cell, write
   the measured values that feed it with their units, show the arithmetic, one or two lines
   per column.

## CON: Conclusion

The instructions for the conclusion are handed out as a numbered list of four or five
questions. Each question gets exactly one sentence, in order, and the sentences form one
paragraph on the board under the header (name, "CON").

1. **The answer to the lab question**, in the form of the QPD question: "The relationship
   between *x* and *y* is [linear / quadratic / a power law of order *n* / polynomial /
   exponential / ...]."
2. **The trendline equation(s)**, with the generic *y = mx + b* rewritten in the lab's own
   symbols and units. Static friction against normal force, for example, is
   *f*<sub>s</sub> = (0.314) *f*<sub>N</sub>, and the coefficient is unitless. Give the
   equation of the relationship graph and of the linearized graph (identical when the
   relationship is linear). When there are several data sets, give every equation: Labs 4
   and 5 had two surface combinations, static and kinetic, so four trendlines.
3. **The result(s)**, with units and context: "The coefficient of static friction between
   cork and poplar is 0.314." All of them when there are several (four coefficients in the
   friction labs, two significant figures in Lab 4's instructions).
4. **Wild card** (not every lab, usually after sentence 3): a quantitative observation the
   instructions ask for, such as "the coefficient of static friction is larger than the
   coefficient of kinetic friction", or "surface combination 1 has the larger coefficients".
5. **The comparison**, usually a percent difference against a known or nominal value;
   sometimes against another measurement or the class mean.

Formulas from the Lab Professor's primer: percent error = 100 % × (M − T) / T against a
true value T; percent difference = 200 % × (M₁ − M₂) / (M₁ + M₂) between two measurements.

## Labs seen so far

- **Lab 4, friction with a force sensor on a flat surface.** Sheet columns: added mass
  M<sub>bars</sub> (given), M<sub>TOTAL</sub> = M<sub>bars</sub> + M<sub>box</sub>,
  F<sub>N</sub> = M<sub>TOTAL</sub> × 9.81, f<sub>s-max</sub> and f<sub>K</sub> read from the
  force-versus-time graph with Statistics boxes. Two surface combinations, 15 trials each.
  Graph: four data sets with four best-fit lines. Conclusion asks for: the relationship in
  words; the four equations in physics symbols; the four coefficients (two significant
  figures) with the surfaces named; static versus kinetic and surface 1 versus surface 2.
- **Lab 5, friction on an incline.** Sheet columns: M<sub>add'l</sub> (given),
  M<sub>TOT</sub>, θ<sub>MAX</sub> in degrees (measured, the angle at which the block starts
  to slip), *a* in m/s² (measured, slope of a *v*–*t* graph in Graphical Analysis),
  F<sub>N</sub> = M<sub>TOT</sub> × 9.81 × cos θ, f<sub>s-max</sub> = M<sub>TOT</sub> × 9.81 ×
  sin θ, f<sub>K</sub> = M<sub>TOT</sub> × 9.81 × sin θ − M<sub>TOT</sub> × *a*. Same
  four-trendline conclusion as Lab 4. The UDA board also needs the derivation of those
  force relationships.
- Source files, ignored by git: `files/26 P1 Lab 4 Analysis Template.xlsx`,
  `files/26 P1 Lab 5 Analysis Template.xlsx`, the two `Report Template.docx` files, and
  `files/Lab Uncertainty Analysis primer1.docx`.

- **Lab 6, the spring constant two ways** (files are the 2025 versions, "25 P1 Lab 6"). Part 1,
  lowering: hang mass M (g) on the spring, lower gently to equilibrium, record y<sub>i</sub> and
  y<sub>f</sub> (cm); Δy (m) = (y<sub>f</sub> − y<sub>i</sub>)/100, F<sub>spring</sub> (N) =
  (M/1000)·9.81; seven rows; graph F<sub>spring</sub> against Δy, linear trendline, slope = k.
  Part 2, dropping: release from the unstretched position, record the lowest point; y<sub>i</sub>,
  y<sub>f</sub> (cm), M (kg), three trials per mass; Δy (m); graph Δy against M, linear; from
  energy, Δy = (2g/k) M, so k = 2g/slope. UDA board: derive F<sub>s</sub> = mg on the left, three
  sample calculations on the right (Δy, F<sub>s</sub>, and k from the second slope). CON: (1) both
  relationships in words, (2) the two equations, (3) both k values, (4) percent difference
  between them, with the lab's own formula %diff = (k₂ − k₁)/k₁. Regular lab (own section only).
- **Whiteboard conventions seen in the example photos** (`files/Lab_Whiteboard_Examples/`,
  ignored by git because real names are visible): job label top left, names top right, a rule
  under the header; the QPD question as a title under a second rule; the UDA board split
  vertically, free-body diagram and derivation on the left, sample calculations on the right.
  Lab 4's CON questions as handed out: relationship between F<sub>N</sub> and friction (both
  f<sub>s</sub> and f<sub>k</sub>); the two static and two kinetic trendlines in physical
  variables; the four coefficients; static or kinetic greater in general; which surface combo
  had the larger coefficients. Lab 4's UDA requirements: data table and four trendlines on one
  graph with the combos labelled; FBD with F<sub>N</sub>, F<sub>g</sub>, f<sub>k,s</sub>,
  F<sub>T</sub>; derive F<sub>N</sub> and f<sub>k,s</sub> from it; example calculation for
  F<sub>N</sub>.

- **Lab 7, impulse and momentum** (2026 files, `26 P1 Lab 7 Momentous analysis template.xlsx` and
  `26 P1 Lab 7 Report template.docx`, added 2026-10-19). Regular lab, but the report says in capitals that
  EVERYONE submits a TWO-PARAGRAPH CON. Part A "Bumper Cart" (sheet: "Impulse-momentum analysis"):
  M<sub>CART</sub> typed into D2, ± 0.001 kg; ten rows of v<sub>init</sub>, v<sub>finl</sub> (m/s, δa 0.01
  given), Impulse (N·s, δa 0.001 given), Dv (m/s, student formula, its δa cell is green); KI = 0.5·M·v<sub>init</sub>²
  and KF = 0.5·M·v<sub>finl</sub>² with a formula in row 4 only (fill down), their own mean/δa/δr cells
  labelled in column N, and a note to add decimal places. Mean row uses −AVERAGE for the negative columns;
  note under v<sub>finl</sub>, Impulse and Dv: "ALL of these should ALL be negative". Graph slots:
  "Velocity Change vs Impulse" (slope → cart mass, CON paragraph 1) and "KINETIC ENERGY comparison"
  KF vs KI (slope vs 1, CON paragraph 2, classify the interaction). Part B "Interaction types analysis":
  M<sub>bar</sub>, M<sub>BLU</sub>, M<sub>YEL</sub> typed into row 19, ± 0.001 kg; nine rows, Bouncy /
  Sticky / Explodey × three mass placements, M<sub>A</sub> = M<sub>YEL</sub> and M<sub>B</sub> = M<sub>BLU</sub>
  with the bar on B in the first row of each trio, on A in the second, on neither in the third (built by
  formula); columns Vi-A, Vf-A, MB, Vf-B (no Vi-B, B starts at rest), DpA and DpB (student formulas),
  KI-A, KF-A, KF-B (KF-B formula in row 22 only), DKA = KF-A − KI-A, DKB = KF-B in column S for the bouncy
  rows and column T for sticky/explodey, and "Bigger Mass: A or B?" in U. Sign notes: Vi-A positive, Vf-A
  mixed, Vf-B positive, DpA negative, DpB positive. Uncertainty colour code: light green inputs (M<sub>A</sub>,
  Vi-A, Vf-A) dictate the dark green DpA cells, light blue (M<sub>B</sub>, Vf-B) dictate DpB ("dark determined
  by light", "green dictates green"); the velocity δa cells are blank in Part B. Graph slot "Momentum Change"
  DpB vs DpA (slope vs −1) plus a pre-built scatter "Kinetic energy Comparison BOUNCY ONLY" (S22:S24 against
  R22:R24, no trendline). Report: two QPD slots (board, annotated setup photo, Graphical Analysis screenshot
  showing where the velocities and, in Part 1, the impulse were read), two UDA slots (table-and-graph
  screenshot; board with THREE calculations for Part 1, Dv, DK and the mass from the slope, FOUR for Part 2,
  Dp and DK for each cart). CON paragraph 1, momentum: (1) relationships in words, (2) the two equations,
  (3) cart mass and the slope compared with −1.00, (4) percent difference M<sub>EXP</sub> vs M<sub>THEO</sub>
  and percent change 1 − |slope|. Paragraph 2, kinetic energy: KF vs KI slope vs 1.00 to classify the wall
  bounce, percent = 1 − slope, and for Part 2 "how kinetic energy change varied BY MASS for the three
  different types of interactions – there are TWO different answers". Page: `lab-guides/07-impulse-momentum.qmd`.

- **Lab 8, balanced and unbalanced torque** (2025 files, `25 P1 Lab 8 Rotation 1 Template.docx` and
  `25 P1 Lab 8 Template.xlsx`, added 2026-10-25). Regular lab. Greek letters in both files are typed in Symbol
  font (q = θ, Dt = Δt, w = ω, a = α). No charts in the sheet. Part 1 "Balanced Torque": seven rows of
  r<sub>b</sub> (m) and F<sub>T</sub> (N), both yellow (typed), with their δa cells yellow too; 1/r<sub>b</sub>
  (1/m) and every mean/δa/δr cell light green and empty (student formulas). Report wants TWO graphs and a UDA
  board with one 1/r sample and the calculation of the unknown pipe radius r<sub>a</sub> "based on the balanced
  torque and the known tension force (F<sub>T</sub> = M<sub>H</sub>g) in the string". The sheet has no cell for
  M<sub>H</sub> or the measured pipe radius. Part 2 "Constant Net Torque" (report: "Unbalanced Torque"):
  seventeen yellow "EDIT time (s)" cells in A17, A19, ..., A49, alternating rows. Mark rows hold t = cumulative
  (B17 = A17−A17, B19 = D18+B17) and θ (C17 = 0, C19 = C17+E18). Interval rows hold Δt = A19−A17, Δθ = `=PI()` in
  a yellow cell, ω = Δθ/Δt, t<sub>MID</sub> = (B19+B17)/2. Formulas exist in rows 17 to 19 only, light blue,
  grey = unused. Means given for t and θ only (B50, C50); δa given as 0.01 for t (B51) and Δt (D51), the rest
  blank. Report: one graph (ω vs t<sub>MID</sub>, linear, slope = α) and a UDA board with one sample each of θ,
  Δt, ω, t<sub>MID</sub>, comparing α with "the acceleration value deduced from your θ-t graph". CON, one
  paragraph: (1) both relationships in words, (2) the two equations, (3) the balancing torque and r<sub>a</sub>,
  then α, (4) %diff = (r<sub>exp</sub> − r<sub>act</sub>)/r<sub>act</sub> and the two values of α. Page:
  `lab-guides/08-torque-rotation.qmd`. The page assumes the apparatus (a hanging mass M<sub>H</sub> on a string
  around the pipe, balanced by F<sub>T</sub> at r<sub>b</sub>, then let go for Part 2) and calls the turning
  part "the rotor".

## Open questions for Saxon

- The rest of the semester's labs, and for each: the question, the measured variables with
  units, the calculated columns, the graph and its linearization, the CON questions and the
  comparison value. Lab 9's topic and what its theory session covers.
- Whether the 2026 Lab 6 differs from the 2025 files.
- Exemplar board photos with names cropped out, for the format page.
- Lab 7: what the professor means by "TWO different answers" for the Part 2 kinetic-energy sentence of
  CON paragraph 2 (the page reads it as bouncy conserving kinetic energy whichever cart carries the bar,
  against sticky losing and explodey gaining it); whether the explodey runs start from rest (the page
  assumes so); and whether "everyone submits CON" is Lab 7 only or the new normal.
- Lab 8: what the apparatus is (bar, disc or platform, and what measures F<sub>T</sub>: force sensor, spring
  scale or hanging masses), what drives Part 2 and how the times are taken, whether the 2026 files differ from
  the 2025 ones, which percent difference to use for the two values of α (the page suggests the primer's
  200 %(α₁ − α₂)/(α₁ + α₂)), and whether δa = 0 for θ and Δθ (the page treats them as counted, exact) is what
  the professor expects.

## Page plan (proposed 2026-10-11, first version built the same day)

Two layers, because students ask two different questions.

1. **One evergreen page, "What goes on each whiteboard"** (`teaching/labs/02-...qmd`),
   answering "does this look okay?". For each job: a drawing of the board at 3:2 with the
   zones marked (header, question, procedure, and so on), a checklist a student can run
   down before photographing the board, and the rules above. For CON, the paragraph as a
   fill-in template with the units slots visible. A units audit as the last item of every
   checklist.
2. **One short page per lab**, answering "what goes in this part for this lab?", all built
   from one template file so writing a new one is mostly filling in front matter: the
   question with *x* and *y* named, a table of measured variables with units, a table of
   calculated columns with formula and units (that is the UDA sample-calculation list), the
   graph and its linearization and how many trendlines, the CON questions one by one with
   the expected form of each sentence and the comparison value, then a short FAQ and a
   "going deeper" section. Quarto's `{{< meta key >}}` shortcode can pull the front-matter
   values into the template sentences, so the CON template reads with this lab's variables
   in place. These pages double as Saxon's own prep notes.
3. Collect two or three real exemplar boards per job over the semester; a photo of a good
   board answers "does this look okay?" better than any description.
