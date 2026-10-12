# VCD 201: evidence pass (third pass), October 12, 2026

Scope: the course plan (`app/seed/plans/vibe-coder-dictionary-intermediate-dp.json`) and chapter 1 (`app/seed/books/vibe-coder-dictionary-intermediate-dp/ch1.json`, figures 2 and 3). Results: `merge_plans.py --write` printed OK; `validate_chapter.py` on ch1 printed "OK: no problems". There are no em dashes.

## Evidence convention (now in bible.conventions, preface paragraph 3, ch1 overview, and a new ch1 slide)

- **(a) Established:** standards, definitions, documented specifications and peer-reviewed findings. These are stated plainly with a citation.
- **(b) Vendor guidance:** what a company's documentation says. It is always attributed and dated ("as of October 2026") and followed by the reasoning that explains why it works. A vendor's claims about its own internal tests are reported as claims, not findings.
- **(c) Practice and opinion:** these statements are marked in the sentence ("in my experience", "practitioners report", "a common explanation, plausible but not stated by..."), together with what is known about whether they hold.
- **Research on older models:** peer-reviewed results carry the model generation and the year, and the text says whether to carry forward the direction of the finding or its numbers.
- **Teaching devices:** the six-part spec is labeled as this book's teaching framework, not an industry standard.
- **Re-checking tool facts:** bible.care now says that tool facts expire and explains how to re-check them. The reader opens the vendor's current page, then runs a small eval: the same prompt on 3 to 5 fixed inputs before and after a change, scored against written criteria.

## Chapter 1 claim counts

These counts cover the reading paragraphs only. They were made by script and checked by hand.

| Kind | Count | Sources and markers |
|---|---|---|
| Established, cited | 11 sentences | ISO/IEC/IEEE 29148, the NASA MCO board, AmbiEnt (EMNLP 2023), Zamfirescu-Pereira et al. (CHI 2023), WCAG 2.2 SC 1.4.3, the Cucumber Book, Min et al. (EMNLP 2022), Sclar et al. (ICLR 2024) |
| Vendor guidance, cited | 21 sentences | Anthropic: prompting guide, Claude Code guide, success criteria page, structured outputs. Also OpenAI GPT-5.5, Runway Gen-4 and Google Imagen. All are now dated October 2026. |
| Practice or opinion, marked | 14 sentences | Explicit markers in the text |
| Definitions | About 25 key terms plus in-text definitions | Not counted as claims |

Key terms, worked examples and practice items follow the same labels.

## Chapter 1: what was reworded or removed

**Dated and explained vendor statements.**
- Every Anthropic, OpenAI, Runway and Google statement now carries "October 2026" or "as of October 2026".
- The text now gives the reasoning behind each piece of vendor advice:
  - Colleague test: the model and the colleague both have only what you wrote.
  - Outcomes rather than steps: a procedure fixes the route.
  - Calm wording: a model that follows the system prompt closely may treat shouting as a cue to apply the rule everywhere.
  - Starting a clean session: failed attempts stay in the context.
- Anthropic's "question last" advice now notes that its internal test method is unpublished.
- The misconception facts in 1.2 and 1.4 and the 1.3 template note are now attributed and dated.
- Slide 6's notes said "Vendors now agree". They now say "OpenAI’s and Anthropic’s guides (October 2026) both favor... vendor guidance, dated, so recheck it."

**Softened or marked as practice.**
- The predicted default game is now "in my experience".
- "Competent and average" is now the everyday experience of prompters, not a finding.
- "Models are poor at catching this" is now tied to the 2023 study, with a caveat that newer models were not measured. "A model picks one reading" is now practitioner report.
- "Negation... models that turn descriptions into pictures handle it especially badly" was generalized from one vendor. It now reads "at least one generator vendor documents that this backfires". The caption-training explanation is labeled plausible but not vendor-stated.
- "Language models cope with negation better" is now "in my experience".
- "Delegating is often right", "a model may add a feature", "if all three sketches are flat..." and the assumption list ("a habit of mine rather than a documented feature") are all marked as practice.
- Criteria-before-results is framed as a lesson testers learn.
- Min et al. now has a caveat about 2022 models and classification tasks. Sclar et al. now has a caveat about 2023 open models, and notes that lower sensitivity in newer models is not established.

**Overclaims fixed.**
- "Tells the model to put its effort into controls and none into graphics" is now "gives the model a reason to...".
- "Gives the model no new information" is now "tells the model you are unhappy but not why". The figure 1.4 label (ch1-fig-3.svg) was changed to match.
- "Will not tell you which hopes it missed" now adds "unless you ask".
- "A model knows only what is in the conversation" now adds files and memory from its tool.
- "Usually the most typical choice" in the Default key term is now "often roughly".

**Inconsistencies fixed.**
- Figure 1.2 (ch1-fig-2.svg) still said "PNG at 1920×1080", which contradicted the recorded correction. It now reads "4 variations as 16:9 PNGs, scaled to 1920×1080 if needed". Figures 1.2 and 1.4 were re-rendered and inspected.
- The sort item "with no echo" (a negation inside an "Exact" sound prompt) is now "dry and close".
- The four-hex-colors item now notes that painted art needs a tolerance, matching the figure 1.3 correction.

**Formal terms added.**
- Constraint, in its requirements sense.
- Non-functional requirement: new key term and paragraph.
- Definition of done: Scrum's term, a new key term with a Lamplighter example.
- Gherkin's keywords: And, But and Feature.
- Zero-shot and one-shot, in the few-shot definition.
- JSON Schema, named as an open standard.

**Other changes.**
- Reference and Counterexample left the 1.3 key-term list to keep it at 6. Both stay bold and defined in the reading.
- 1.3 gained a seventh paragraph, and other paragraphs were trimmed to stay at or under 170 words.
- New slide: "Three kinds of claim, and keeping them current", which includes how to recheck a tool fact. There are now 12 slides.

**Prompt kit.**
- All 11 templates were kept.
- None asserted a tool behavior as fact beyond notes that were already dated.
- The "Scoped revision request" note now attributes the two-corrections rule to Anthropic (October 2026).

**Review block.**
- It was deleted.
- All ten recorded corrections are still in the text: figure numbers, Opus 4.5/4.6 attribution, positive-phrasing templates and answers, the 16:9 output, the eight-decision list, and "mostly the 4 palette colors". The attribution sentence only gained "as of October 2026".
- `ch1.check.json` was left untouched.

## Plan changes

**Front matter.**
- Description: names the standards backbone and the three kinds of claim.
- Objective 1: names requirements terms.
- Objective 3: adds telling established findings from vendor guidance and lore.
- The preface gained a third paragraph explaining the convention, plus a grain-of-salt note.
- Two preface claims were softened:
  - "A language the model already knows" now reads that the vocabulary is public writing models learn from, so people and models tend to read it the same way.
  - "Tips no longer help" now reads that vendors now advise against them.

**Teacher, threads and conventions.**
- The teacher entry names the standards backbone.
- Thread 5 states the evidence convention.
- Four convention entries were added at the top, plus a "reference shelf" entry listing non-canon references with dates.

**Chapters 2 to 12.** Summaries and key sections now name each field's durable vocabulary, standards and texts:

| Chapter | Durable vocabulary, standards and texts |
|---|---|
| 2 | Tokenization, nucleus sampling (Holtzman 2020), chain-of-thought research, lost in the middle versus context rot (a practitioner term) |
| 3 | Persona evidence, JSON Schema 2020-12, myths rated by evidence |
| 4 | HTTP methods and status codes, Semantic Versioning, Git terms from Pro Git |
| 5 | Least privilege, MCP as dated vendor docs |
| 6 | WCAG 2.2 SC 1.4.3, 2.4.7 and 2.5.8; WAI-ARIA 1.2; CSS easing; slow in and slow out |
| 7 | Film-grammar shot sizes, focal length in millimetres, three-point lighting, kelvin |
| 8 | Bordwell and colleagues, SMPTE timecode rates, the twelve principles, animating on ones and twos |
| 9 | BS.1770, EBU R 128 at −23 LUFS, SSML 1.1 elements, IPA |
| 10 | MDA, Fullerton's formal elements, Swink; practitioner terms labeled |
| 11 | glTF 2.0 / ISO/IEC 12113, the metallic-roughness maps, metres and +Y up |
| 12 | 29148 traceability, definition of done, SemVer for prompts; spec-driven development labeled as a recent practitioner and vendor method |

**Canon.** The canon was rebuilt and is still at 10.
- Added: ISO/IEC/IEEE 29148:2018; Thomas and Johnston (1981); ITU-R BS.1770-5 (2023); Hunicke, LeBlanc and Zubek (2004); ISO/IEC 12113:2022 (glTF 2.0).
- Kept: the Anthropic prompting guide, WCAG 2.2, Bordwell and colleagues (13th ed.), Schell, and Swink.
- Moved to the reference shelf: Claude Code best practices, OpenAI GPT-5 guide, Google Gemini guide, Tidwell and colleagues, and Senior.
- Each canon role now says which kind of claim it supports.

**Care and provenance.**
- The care text adds that tool facts expire and explains the recheck method.
- Provenance was bumped to dp-0.7.

## Verification notes (20 web searches, October 12, 2026)

| Reference | What was confirmed | Strength |
|---|---|---|
| ISO/IEC/IEEE 29148:2018 | 2nd edition, 2018-11; the nine individual-requirement characteristics | Secondary (arXiv 2408.10886, vendor pages); the standard is paywalled |
| ITU-R BS.1770-5 | Approved 2023-11-22, in force; a revision is in drafting | itu.int record |
| EBU R 128 v5.0 | November 2023; −23 LUFS, ±0.5 LU | tech.ebu.ch |
| ISO/IEC 12113:2022 | "Runtime 3D asset delivery format: Khronos glTF 2.0", edition 1, July 2022 | ISO catalog |
| glTF "2.0.1" | Not confirmed, so not cited | |
| MDA | 2004 AAAI Workshop on Challenges in Game AI, pp. 1–5 | Paper copy and the author's CV; the AAAI page was not opened directly |
| SSML 1.1 | W3C Recommendation, 7 September 2010 | w3.org |
| WAI-ARIA 1.2 | W3C Recommendation, 6 June 2023 | w3.org |
| Semantic Versioning 2.0.0 | MAJOR.MINOR.PATCH | semver.org; authorship was not confirmed in the results, so it is cited by title |
| Pro Git 2nd ed. | Chacon and Straub, Apress, 2014 | Springer listing |
| JSON Schema | 2020-12 is the current version | json-schema.org |
| Scrum Guide 2020 | Definition of Done wording | Secondary quotes of the official text |
| ISO/IEC 25010:2023 | Usability renamed interaction capability | Secondary |
| SMPTE ST 12-1 | Nominal rates including 23.98, 24, 25, 29.97, 30, 50, 59.94, 60 | SMPTE overview and secondary sources |
| Cucumber Gherkin reference | Feature, Scenario, Given, When, Then, And, But | cucumber.io excerpt |
| Thomas and Johnston | 1981, Abbeville Press | Secondary |
| Williams | Expanded edition 2009, Faber and Faber | Library records |
| Fullerton | *Game Design Workshop*, 5th ed., 2024, CRC Press | Routledge |

Not searched this pass, stated from expert knowledge in plan summaries only:
- WCAG SC numbers 2.4.7 and 2.5.8.
- Fullerton's list of formal elements.
- glTF's use of metres and +Y up.
- Holtzman et al. (2020), Wei et al. (2022), Kojima et al. (2022) and Zheng et al. (2024). These appear in the LLM research brief.

The chapter writers should verify these against primary sources when chapters 2 to 12 are written.

## Plan check (independent fact-check, October 12, 2026)

An independent second agent checked the plan's canon entries and the standards named in the chapter summaries, focusing on the items listed above as unverified. It used about 20 web searches. Khronos, OpenAI, Runway and Google hosts could not be fetched directly: the proxy returned CONNECT 403. Results:

| Item | Result | Basis |
|---|---|---|
| WCAG 2.2 SC 2.4.7 Focus Visible; SC 2.5.8 Target Size (Minimum), 24 by 24 CSS px, Level AA | Correct as named | W3C "What's New in WCAG 2.2" and Deque/DAISY excerpts; 2.4.7 from expert knowledge |
| Fullerton's formal elements (players, objectives, procedures, rules, resources, conflict, boundaries, outcome) | Correct, eight elements | University lecture slides and a thesis citing the 5th ed. (2024) |
| glTF 2.0: metres, +Y up | Correct (right-handed, Y-up, metres) | Secondary excerpts pointing to the spec's "Coordinate System and Units" section |
| EBU R 128 −23 LUFS; ITU-R BS.1770-5 (2023); ISO/IEC 12113:2022 | Correct | Earlier pass's primary records; not contradicted |
| SSML 1.1 (7 Sept 2010); WAI-ARIA 1.2 (6 June 2023) | Correct | Expert knowledge, matching earlier pass |
| SMPTE ST 12-1 rates | Correct: ST 12-1:2014 covers 23.98, 24, 25, 29.97, 30, 47.95, 48, 50, 59.94, 60 fps (48 and 47.95 added by the 2013 amendment) | GlobalSpec abstract |
| Thomas & Johnston (1981), Abbeville Press, twelve principles | Correct; role reworded (fix 2) | Expert knowledge |
| Hunicke, LeBlanc & Zubek (2004), MDA | Authors, year, workshop and AAAI Technical Report WS-04-04 confirmed. Page range "pp. 1–5" not confirmed, so replaced (fix 1) | AAAI workshop page, author CV, grandtextauto |
| Holtzman et al. (ICLR 2020); Wei et al. and Kojima et al. (NeurIPS 2022) | Correct as named | Brief (arXiv) and expert knowledge |
| Zheng et al. (2023), LLM-as-a-judge | NeurIPS 2023 Datasets and Benchmarks Track confirmed. The brief's "[Unverified]" venue note can be cleared | proceedings.neurips.cc and neurips.cc poster page |
| Zheng et al. (2024), personas (plan ch3 §3.1) | Findings of EMNLP 2024; fine as "Zheng and colleagues, 2024" | Brief |
| Bordwell, Thompson & Smith, 13th ed. | 2024 copyright (released October 2023); 2024 kept | Library catalogs, McGraw Hill listings |
| Senior, *Mixing Secrets*, 3rd ed. (2025) | Confirmed, Routledge, September 2025 | Routledge author page, booksellers |
| Care text: prefill and non-default temperature errors on newest Claude models | Consistent with the live Prompting best practices page (prefill unsupported from Claude 4.6) and the LLM brief (temperature, Opus 4.7+) | Live page |

**Plan fixes made** (JSON still valid; `merge_plans.py --write` printed OK):

1. **Canon[6], MDA citation.** Before: "In Proceedings of the AAAI Workshop on Challenges in Game AI (pp. 1–5). AAAI Press." After: "In Challenges in Game AI: Papers from the 2004 AAAI Workshop (Technical Report WS-04-04). AAAI Press." The technical-report number is confirmed; the page range is not.
2. **Canon[4], Thomas & Johnston role.** Before: "The source of the twelve principles of animation". After: "The book that first set out in print the twelve principles of animation developed at the Disney studio". The principles came from studio practice in the 1930s; the 1981 book published them. It did not originate them.
3. **Preface paragraph 1.** Before: "an AI trained on their writing understands those names. Much of that writing is public, and models learn from public text, so when you say..." After: "much of their writing is public text of the kind models learn from. So when you say...". The old wording stated what a model "understands" as fact, which breaks convention (c). The rest of the sentence already gave the hedged version.

No other plan detail was found to be wrong. The chapter-level findings are in `ch1.check.json` (12 corrections, no key fixes).
