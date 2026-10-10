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

## 6. Visual design: the reading room

- **Mood.** A library reading room: warm paper and lamplight by day, walnut and brass after hours (dark mode). Paper grain and a lamp glow behind the page.
- **Books, not cards.** Every course is a library-bound book: bookcloth color (forest, navy, oxblood, plum, teal, leather), gilt panel rules, a gold-foil cover emblem, a title in Caslon, and the author's name. They stand on wooden shelves in the catalog.
- **Type:**
  - Libre Caslon Display for titles: the classic book face.
  - Literata for reading: designed for long-form screen reading.
  - Source Sans 3 for controls.
  - Courier Prime for catalog details (call numbers, labels).
- **Library details:**
  - The request form is a catalog card (red top rule, faint ruled lines, punch hole).
  - Fact-checked chapters carry an ink stamp.
  - Each chapter is laid out as a page on the desk.
- **Color-coded textbook boxes:** objectives (book color), key terms (blue), worked example (green), practice (amber), misconception (oxblood), fact-check (violet).
- **Figures are full-color illustrations** where color carries meaning, using a field's standard colors where they exist (ICS geologic-period colors).

## 7. Authors and personal tutoring

**The textbook is shared; the tutoring is personal.** A book is written once, in one author's voice, and everyone reads the same fact-checked text. Around it sits a private tutoring layer tuned to each learner.

| Author | Voice |
|---|---|
| The Scholar | Formal, rigorous, evidence first, history of ideas |
| The Kindergarten Teacher | Warm, very simple words, concrete; facts stay exact |
| Socrates | Teaches by questions; you reason your way to each idea |
| The Brainiac | Dense, fast, cross-disciplinary |
| The Straight Shooter | Plain and short: the fact, then why it matters |
| The Storyteller | Through the true people and discoveries behind ideas |
| The Practitioner | How the work is actually done, common mistakes |

- **No AI voice.** Every prompt carries a style guide that bans stock AI phrasing (delve, tapestry, crucial, em dashes, rule-of-three habits, summarizing morals). A built-in style checker counts leftovers, and the fact-check rewrites them.
- **Study profile** (private): favorite tutor, how you learn best (reading, diagrams, worked examples, practice, discussion, listening, stories, real-world use), goal, background and daily study time.
- **Explain it differently:** any section can be re-explained by any author for you. The re-explanation uses your profile and targets your wrong answers in that section.
- **Study coach:** your accuracy per section is tracked from practice and quizzes. For weak sections it writes a personal review sheet: the idea you are missing, why your wrong answer was tempting, a fresh example, a new check question, and a plan for your next session.
- Office hours also use your profile.

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

## 11. What's built now (prototype v0.3)

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
