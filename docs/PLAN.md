# Dr. Professor: vision and plan

> A full course on any subject, at any level, on demand. A textbook and a workbook in one, with lectures, figures, practice, exams and a certificate.

Origin: John's long-standing idea, and Jack's prompt (Discord, 11/29/2025):

> Create a listed glossary of chapters in a hypothetical textbook for learning X most effectively … in the context that I am a (new student, advanced student, intermediate, master). The hypothetical holy grail of learning material needs to be both a textbook and a workbook: introduce per chapter and per subsection practice problems as well as end of chapter challenge exercises, and integrate these units into the linear hierarchy of the hypothetical textbook chapter glossary. … Now actualize the textbook's structure, realize each chapter, populate each chapter with the textual and study materials that will best capture the outline into real learning materials.

Aaron called it "automatic Khan Academy." Jack's warning matters as much as the idea: the tool is only worth it while it produces value **you can put in your pocket**, meaning real knowledge and skill, not time spent in an interface. Design every feature against that test.

---

## 1. Principles

1. **Information first, and plain.** The look is a college course catalog and a textbook page. No mascots, streaks or confetti. Tables, ruled lists, serif reading text, monospace course codes.
2. **Textbook and workbook in one.** Every section ends in practice. Every chapter ends in a quiz and harder challenge exercises. The order is linear, like a real book.
3. **Level is a first-class input.** The same subject at Noob and at Mastery are different courses: different vocabulary, math, sources and exercises.
4. **Several ways to learn the same thing.** Reading, figures, worked examples, a lecture deck, retrieval practice, applied challenges, discussion (office hours), outside reading, video and images.
5. **Honest about sources.** Dr. Professor never makes up a URL. Citations come with a "verify" search link. Videos and images are search links until a real retrieval pipeline exists (see §6).
6. **Write once, share.** A chapter is generated once and saved to a shared library. Everyone taking that course sees the same text and takes the same exam. That keeps costs down and makes certificates comparable.
7. **Earned credentials.** The certificate states its basis: full coursework plus the final, or credit by examination.

## 2. Levels

| Level | Course no. | Who it's for | How the material changes |
|---|---|---|---|
| Noob | 050 | Zero background | Everyday language, analogies, every term defined, intuition before vocabulary |
| Beginner | 101 | First real course | Core vocabulary, clear examples, light numbers |
| Intermediate | 201 | Knows the basics | Mechanisms, standard models, quantitative reasoning, field methods |
| Advanced | 301 | Upper-division | Formal tools (equations, frameworks), edge cases, standard texts |
| Expert | 501 | Graduate | Current research, competing models, primary literature |
| Mastery | 701 | Frontier / master practitioner | Open problems, judgment calls, original synthesis, teach-back exercises |

**Ideas to add later:** a 10-question **placement test** that recommends a level, and **level shifting**, where a stuck learner can re-explain a section one level down.

## 3. Course anatomy (Jack's hierarchy, made concrete)

```
Course  (code, title, catalog description, prerequisites, objectives, est. hours)
├── Chapter 1..N
│   ├── Overview + learning objectives
│   ├── Lecture deck (8–12 slides + lecturer's notes)
│   ├── Section n.1..n.4
│   │   ├── Reading (textbook prose)
│   │   ├── Figure(s) (diagram, cutaway, timeline, graph)
│   │   ├── Key terms
│   │   ├── Worked example (step by step)
│   │   ├── Practice n.x (3 problems: multiple choice + short answer, at least one applied)
│   │   └── Margin notes (learner's own)
│   ├── Chapter quiz (8 questions, 70% to pass)
│   ├── Challenge exercises (2, graded against a rubric by Dr. Professor)
│   ├── Homework reading (real, verifiable sources + "find it" links)
│   ├── Watch and look (video and image searches)
│   └── Office hours (ask questions about this chapter)
├── Final examination (16 questions across all chapters, 75% to pass)
├── Certificate (basis: coursework and examination, or credit by examination)
└── Notebook (all notes and submissions, exportable as Markdown)
```

## 4. Learning methods and where each lives

| Method | Why it works | Where |
|---|---|---|
| Reading | Builds the mental model | Section prose |
| Dual coding | Words plus pictures stick better | Figures in each chapter |
| Worked examples | Show the procedure before asking for it | One per section |
| Retrieval practice | Testing yourself beats rereading | Practice problems, quizzes |
| Elaboration | Explaining in your own words | Notes, short-answer practice |
| Application / transfer | Use ideas on new cases | Challenge exercises |
| Lecture | A second pass in a different form | Slide deck + notes |
| Dialogue | Fix your own misconceptions | Office hours |
| Spaced repetition | Recall at increasing intervals | **Planned:** key-term flashcards scheduled across days |
| Primary sources | Real expertise lives there | Homework reading |
| Observation / lab | Learning that leaves the screen | Challenge prompts that send you outside (birding, sky diary) |

## 5. Accuracy system

Accuracy is the first requirement. A learner relies on every sentence.

1. **Writing rules.** Every prompt tells Claude to state only well-established facts. It must never invent statistics, studies, quotes, dates or sources, should round or omit figures it is unsure of, and should separate consensus from open debate.
2. **Fact-check pass on every chapter.** After writing, a second pass on Claude's most capable model checks every claim, figure label, slide, explanation and citation. It returns exact text spans and their corrections, which are applied automatically.
3. **Blind answer-key check.** Every multiple-choice question (practice, quizzes, final) is re-solved without the key. Any disagreement goes to a third pass that decides the correct answer, or rewrites the question if it has two defensible answers.
4. **Citation screening.** Readings judged likely invented are removed, and uncertain ones are labeled "Unverified." Every reading links to WorldCat or Google Scholar so you can confirm it.
5. **Fact-check report** at the top of every chapter: the date, the answer-key agreement, and every change before and after, with the reason.
6. **Learner error reports.** "Report an error" under each section. Dr. Professor checks the report, fixes the text if the report is right (or explains if it isn't), and logs the change in the report.
7. **The seed chapter** (ORN 101 Ch. 1) was checked by an independent agent against published sources. It found 1 factual error and 23 imprecise wordings, all corrected; 16/16 answer keys were confirmed.

**Limit:** the in-app fact-check uses Claude's own knowledge; it cannot look anything up. The standalone app (v1.0) adds web search and citation lookups (Crossref, Open Library) to the fact-check.

## 6. Visual design

- **College textbook, in color.** Each course has a subject color carried through the course cover, the chapter opener (large chapter number), key terms in the text, slide headers and figure numbers.
- **Color-coded boxes,** the same in every course:
  - Objectives (subject color)
  - Key terms (blue)
  - Worked example (green)
  - Practice (amber)
  - Common misconception, Myth vs. Fact (red)
  - Fact-check (purple)
- **Figures are full-color illustrations** where color carries meaning: parts colored by region, labels matching their parts, and the field's standard colors where they exist (ICS colors for geologic periods).
- Works in light and dark mode and at phone width.

## 7. What's built now (prototype v0.2)

`app/dr-professor.html` is a single-page app published as a private Claude artifact. Courses are written live by Claude on the viewer's own account through the artifact `sample` capability.

- **Catalog:** shared course library plus a request form (subject, level, focus, length: 5, 8 or 12 chapters).
- **Syllabus generation:** about one minute. Produces the course code, catalog entry, objectives, and chapters with sections.
- **Chapter generation on demand,** in three parallel parts (text and practice / figures / lecture and assessments). Each part is saved as it finishes; a failed part can be retried alone.
- **Chapter reader:** contents rail, lecture deck, sections, SVG figures, key terms, worked examples, practice with instant feedback, notes, read-tracking.
- **Assessments:** quiz with explanations, challenge grading with a rubric table, final exam, certificate saved as SVG.
- **Office hours:** chat scoped to the chapter text.
- **Transcript and notebook** (private to each viewer); notes export as `.md`.
- **Storage:** the shared library is in the artifact database (`courses/…`); progress is in the private `data/users/<id>/…`. The app falls back to browser storage when opened outside Claude.

**Seed library** (in `app/seed/`, built with `scripts/build_seed.py`):

| Code | Course | Level | State |
|---|---|---|---|
| ORN 101 | Birds: Anatomy, Behavior, and Field Identification | Beginner | Syllabus + Chapter 1 written by hand as the quality bar and independently fact-checked (3 color figures, 4 misconception boxes, 12 practice problems, 9 slides, 8-question quiz, 2 challenges) |
| GDS 201 | Game Design: Systems, Mechanics, and Player Experience | Intermediate | Syllabus; chapters generate on open |
| AST 050 | Outer Space from the Ground Up | Noob | Syllabus (short, 5 chapters) |
| ENR 301 | Energy Systems: Conversion, Storage, and the Electric Grid | Advanced | Syllabus |

### Known limits of the prototype
- **Figures** are SVG diagrams Claude draws. Fine for schematics, timelines and graphs, but not photos. Quality varies.
- **No embedded video or photos.** The artifact sandbox blocks external images and iframes, so these are search links.
- **Citations** are from model memory. They carry a "Find it" link and a warning, and are not verified.
- **Grading** is by the model against a rubric. It's useful feedback but not proctored.
- **The final exam is open-book** and can be retaken. The certificate is a record of completion, not an accredited credential.

## 8. Roadmap

**v0.2: make it feel like a course**
- Placement test → level recommendation.
- Spaced-repetition review queue built from key terms and missed questions.
- Per-chapter "explain it one level down / one level up" toggle.
- Regenerate one section, with a reason ("too easy", "wrong", "more examples").
- Error reports from learners ("this fact is wrong"), stored and fed into the next regeneration.

**v1.0: standalone app (beyond the artifact sandbox)**
- Backend (e.g. Next.js on Vercel + Supabase) with the Claude API, prompt caching for syllabus context, and batch generation of whole courses.
- **Real media pipeline:**
  - Images from Wikimedia Commons, NASA Image Library, Smithsonian Open Access, Macaulay Library, with license and attribution.
  - Videos via the YouTube Data API, filtered to channels from universities, museums and agencies; embedded, with timestamps.
  - Generated narrated slide videos (TTS over the lecture deck).
- **Citation verification:** check books against Open Library/WorldCat, papers against Crossref/DOI, and drop anything that doesn't resolve.
- Web search during generation, for subjects that change fast.
- Printable PDF textbook and workbook per course.
- Accounts, classes (Jack and John take the same course and compare transcripts), shareable certificate verification page.

**Later**
- Labs and simulations per subject (e.g. orbit sandbox for space, circuit/grid sim for energy, game-loop prototyping for game design).
- Audio lessons for birding by ear.
- Instructor mode: edit and lock a course, then publish it to a class.

## 9. Open questions for John and Jack

1. **Who is it for first:** you two, or the public? That decides whether the artifact is enough or v1.0 is needed.
2. **Certificate weight:** should it require full coursework (no credit by exam)? Should the final be timed?
3. **Shared or personal courses:** one shared "Birds 101" for everyone, or a course tailored to each person's focus? (The prototype shares by default and records the focus in the course.)
4. **Media priority:** real photos and video (needs the v1.0 backend) or generated diagrams and slide videos first?
5. **Cost:** generation runs on each viewer's Claude account in the prototype. A public app would need API billing.

## 10. How to test the prototype

1. Open the artifact link and go to **ORN 101 → Chapter 1** to see the target quality.
2. Open **GDS 201 → Chapter 1** and press **Write chapter 1** to watch it generate live (one to three minutes).
3. Request a new course from the form: try the same subject at Noob and at Expert and compare.
4. Take the Chapter 1 quiz, submit a challenge for grading, and ask a question in office hours.
5. Sit the final for a course (credit by examination) and save the certificate.

Note what feels wrong in each step (accuracy, level fit, pacing, missing learning modes). That is the input for v0.2.
