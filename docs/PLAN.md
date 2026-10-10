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

## 6. Visual design: a personal study app

- **It's John's app, not a catalog.** Four tabs (Desk, Library, Review, Profile) along the top on desktop, and as a bottom tab bar on phones.
- **Desk (home):**
  - a greeting;
  - **Continue reading** (cover, chapter, progress, Resume);
  - **Today's review** (cards due);
  - a profile prompt until it's filled in;
  - **Learn something new** (one input);
  - **Your books**;
  - a short "How Dr. Professor teaches".
- **Library:** the shelf of book covers, plus a **New book** flow. It's one question ("What do you want to learn?"), level chips and Dr. Professor as the recommended author; everything else sits under "More options".
- **Book page:** cover, progress, Continue button, a contents list with status, then the coach and "About this book". Objectives, preface and edition record are collapsible.
- **Look:** calm warm surfaces, rounded cards and 44px touch targets. Literata for reading and headings, Source Sans 3 for the interface, Libre Caslon Text for the gilt cloth book covers. Light and dark themes.

## 7. One teacher, coherent books

**Every book has one author, Dr. Professor:** a world-class expert in that subject with deep, wide knowledge of its history, evidence, methods and open questions, who is also an engaging teacher. The character voices from v0.3 are gone, because they risked uneven writing.

**A book bible keeps each book coherent.** It's drafted with the syllabus and stored on the book:
- **teacher:** the expert stance for this subject (for example, "as an ornithologist would: from museum specimens, field observation, experiments and the fossil record").
- **promise:** what the reader will be able to do by the end.
- **threads:** two to four ideas that run through every chapter.
- **running examples:** real cases revisited across chapters (the American Robin through the whole Birds book; *Tetris*, *Super Mario Bros.* 1-1 and *Slay the Spire* plus the reader's own pocket card game in Game Design; one scale model of the solar system; one kilowatt-hour followed from source to socket).
- **conventions:** names, units and notation.

**Continuity.** When a chapter is written, the prompt includes what earlier chapters already taught (their overviews and key terms), so chapters build on each other and refer back by number instead of re-teaching. Every chapter opens with a true, vivid **hook**.

**Personal tutoring uses teaching modes, not characters.** Any section can be explained again Simpler, Deeper, With an analogy, Step by step, Through a real example, or as The story behind it. The study profile stores a preferred mode.

## 7b. Interactive lab

These are built-in components. Chapters supply only data, and a small arithmetic parser evaluates explorer formulas, so AI-written code never runs.

| Type | What the learner does | Example |
|---|---|---|
| Explorer | Moves sliders; outputs update from real formulas | Lift vs airspeed and wing area; Carnot efficiency vs temperatures |
| Sort it | Puts items in buckets, with instant feedback and reasons | Bird or not a bird; energy vs power |
| Put in order | Taps steps into sequence, then sees the right order | One breath through a bird's air sacs; the Rankine cycle |
| Timeline | Clicks events on a real time axis | Feathered dinosaurs to modern birds |
| To scale | Compares real quantities, linear or log | Hummingbird to ostrich mass; planet sizes |
| Case study | Thinks, then reveals each step of a real case | Identifying a mystery bird; the Pluto decision |

Generated chapters now include 2-3 interactives, designed together with the figures.

## 7c. How the seed books are written (research pipeline)

The seed books are researched and written in Claude Code, so they can be read right away:
1. A **book bible** per book (`app/seed/courses.json`) and a strict **chapter spec** (`docs/CHAPTER_SPEC.md`).
2. One **research-and-writing agent per chapter**. It verifies every fact and citation by web search, draws figures and looks at its own renders, builds interactives, and must pass `scripts/validate_chapter.py` (structure, citations, answer keys, banned AI phrasing, formulas).
3. One **independent fact-check agent per chapter**. It re-solves every answer key blind and checks every claim, figure label, formula and citation. `scripts/apply_check.py` applies the corrections and records each change in the chapter's fact-check report.
4. `scripts/build_seed.py` assembles the books, and they are loaded into the app's shared library.

### Learning methods built in (v0.4)
| Method | What it is | Where |
|---|---|---|
| Pretest | "Before you read: take a guess" on each section; guessing first makes the answer stick | Top of every section |
| Worked examples | The idea shown step by step before you try it | Each section |
| Retrieval practice | Practice problems and quizzes | Each section, each chapter |
| Explain it back | You teach the section in your own words; Dr. Professor scores it and lists what you got, missed and got wrong | After each section's practice |
| Spaced review | Flashcards (key terms of sections you finish, plus every question you miss) return at growing intervals; Again/Hard/Good/Easy ratings | Review tab, Desk |
| Interleaving | Review cards from all books are mixed into one session | Review tab |
| Coaching | Weak sections re-explained and a review sheet aimed at your mistakes | Book page |

## 8. Provenance: who wrote what

- **"About this edition"** page in every book records:
  - the author voice;
  - that Claude by Anthropic wrote it, with the engine tier that actually answered each part (Standard or Most capable);
  - dates and who requested it;
  - the prompt version and the sources policy.
- **Each chapter** has a "Who wrote this chapter" line covering text, figures, assessments, fact-check and narration, with engine, date and requester.
- **The sample books** record that they were hand-written in Claude Code and verified by independent agents.

## 9. Audio editions

- **Now:** a read-aloud player using the device's best voice. It ranks Premium, Enhanced, Natural and Neural voices first and skips novelty voices, and offers speed, voice choice, a clickable transcript and a saved position. The **narrated edition** is the chapter rewritten for listening by its author: figures described aloud, citations dropped, units spoken naturally, sections announced.
- **Voice quality depends on the device.** It is excellent with Edge "Natural" voices and with Apple Premium or Enhanced voices; basic elsewhere. The player says how to get a better voice.
- **Next (studio narration):** pre-rendered audio files from a high-quality voice service (for example ElevenLabs, OpenAI TTS, or the Higgsfield connector already on this account), stored as artifact assets. This costs per minute of audio, so it needs an explicit go-ahead.

## 10. Scholarly data sources (APIs)

These are free scholarly APIs Dr. Professor should use. **Constraint:** a published Claude artifact cannot call outside websites (the page's security policy blocks it), and Claude's in-page model has no web access. So they need a small bridge.

| Purpose | API | Use in Dr. Professor |
|---|---|---|
| Papers, citations, DOIs | **OpenAlex** (250M+ works, free, no key), **Crossref** (every DOI) | Verify every citation exists; fill in missing DOIs, volumes and pages; find the most-cited sources for a topic |
| Paper search and summaries | **Semantic Scholar** (free key) | Suggest the strongest sources before writing; get abstracts so claims match papers |
| Biomedical | **PubMed / NCBI E-utilities**, **Europe PMC** | Medical and biology courses |
| Preprints | **arXiv** | Physics, CS, math frontier chapters (Expert, Mastery) |
| Free full text | **Unpaywall** | Link each cited paper to a legal free copy |
| Books | **Open Library**, Library of Congress | Verify textbooks and editions; cover and ISBN data |
| Images | **Wikimedia Commons**, **NASA Image Library**, **Smithsonian Open Access**, Biodiversity Heritage Library | Real photos and historical plates with license and attribution |
| Subject data | **GBIF**, **eBird** (birds), **Xeno-canto** and Macaulay Library (bird songs), NASA ADS (astronomy) | Range maps, real observations, actual bird recordings for "birding by ear" |
| Facts | **Wikidata** | Cross-check dates, quantities and names |

**Bridge options:**
1. **A "Scholar" connector (recommended next step).** A small MCP server deployed on Vercel exposes tools like `search_works`, `verify_citation`, `find_images` and `get_recording`, backed by the APIs above. John adds it once as a custom connector in claude.ai. The artifact then calls it through the `mcp` capability, and the fact-check can look things up for real. This needs John's approval for the deployment and the connector.
2. **Standalone app (v1.0).** Next.js on Vercel with the Claude API calling the same APIs server-side. It's needed anyway for public use, real accounts and billing.

## 11. What's built now (prototype v0.4)

`app/dr-professor.html` is a single-page app published as a private Claude artifact. Books are written live by Claude on the viewer's own account through the artifact `sample` capability.

- **The shelf:** a shared library of book covers, plus a catalog-card request form (subject, level, author, focus, length, writing engine).
- **Front matter:** generated cover art in gold foil, title page, preface in the author's voice, objectives, contents, and "About this edition".
- **Back matter:** glossary (A to Z, linked to sections) and bibliography (deduplicated, with fact-check status).
- **Chapters,** written in three parallel parts plus a fact-check pass:
  - text with numbered citations and per-section sources;
  - worked examples, misconception boxes and practice;
  - color figures, a lecture deck, a quiz tagged by section, challenges, readings and watch-lists.
- **Accuracy:** fact-check of claims, labels, citations and style; answer keys re-solved blind and disputes adjudicated; a report showing every change; learner error reports that check and fix the text.
- **Tutoring:** study profile, "explain it differently", study coach with personal review sheets, office hours.
- **Audio edition:** read-aloud player plus the narrated edition.
- **Assessments:** quizzes, graded challenges, final exam with verified key, certificate.
- **Storage:** the shared library lives in the artifact database (`courses/…`). Progress, notes, tutoring and profile live in private `data/users/<id>/…`. Opened outside Claude, the app falls back to browser storage.

**Seed library** (in `app/seed/`, built with `scripts/build_seed.py`):

| Code | Book | Level | Author | State |
|---|---|---|---|---|
| ORN 101 | Birds: Anatomy, Behavior, and Field Identification | Beginner | The Scholar | Chapter 1 hand-written as the quality bar: 22 cited sources (15 with confirmed DOIs), fact-checked and citation-verified by independent agents |
| GDS 201 | Game Design: Systems, Mechanics, and Player Experience | Intermediate | The Practitioner | Syllabus, preface, cover |
| AST 050 | Outer Space from the Ground Up | Noob | The Kindergarten Teacher | Chapter 1 generated live by John with v0.2: 14/14 keys confirmed, 2 corrections |
| ENR 301 | Energy Systems: Conversion, Storage, and the Electric Grid | Advanced | The Brainiac | Syllabus, preface, cover |

### Known limits
- The in-app fact-check works from Claude's knowledge; live lookups need the Scholar connector (§10).
- No embedded photos or video yet (sandbox); these are search links until the bridge exists.
- Audio quality depends on the device's voices until studio narration is added.
- Grading is by the model against a rubric. The certificate records completion and is not an accreditation.

## 12. Roadmap

**Next**
- Scholar connector (OpenAlex, Crossref, Semantic Scholar, Unpaywall, Wikimedia, GBIF, Xeno-canto) wired into writing and fact-checking.
- Studio narration (pre-rendered audio) once a voice service is approved.
- Placement test that recommends a level and author.
- Spaced-repetition queue from key terms and missed questions.
- "Explain one level down / up" for any section.
- Printable PDF book and workbook.

**v1.0: standalone app**
- Next.js on Vercel with Supabase and the Claude API: prompt caching, batch generation of whole books, real accounts, classes (Jack and John on the same course), and certificate verification pages.

**Later**
- Labs and simulations per subject (orbit sandbox, grid dispatch sim, game-loop prototyper).
- Birding by ear with real recordings.
- Instructor mode.

## 13. Open questions for John and Jack

1. **Scholar connector:** OK to deploy a small MCP server on Vercel and add it as a connector? It unlocks real citation lookups and images.
2. **Studio narration:** which voice service, and what monthly budget?
3. **Who is it for first:** you two, or the public?
4. **Certificate weight:** require full coursework, or allow credit by examination?
5. **Default author:** should the app suggest an author from the study profile automatically?

## 14. How to test

1. Open the shelf and pick **ORN 101**. Read the front matter, then Chapter 1: click a citation number, open the fact-check report, press Play in the audio edition, then try "Explain 1.2 differently" as Socrates.
2. Set up your **Profile** (favorite tutor, how you learn), then get a few practice questions wrong and open the **Study coach** on the book page.
3. Commission a new book with a different author, and compare the voice.
4. Open **GDS 201 Chapter 1** and write it; watch the fact-check report and the citations appear.
