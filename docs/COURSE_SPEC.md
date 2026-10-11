# Course plan spec (Dr. Professor seed books)

One JSON file per course in `app/seed/plans/<id>.json`, merged into `app/seed/courses.json` by
`scripts/merge_plans.py`. Chapters are then written with the pipeline in `docs/CHAPTER_SPEC.md`
(writer agent, independent fact-check agent, `apply_check.py`, `build_seed.py`).

```json
{
 "id": "particle-physics-advanced-dp",          // <topic-slug>-<level>-dp
 "v": 1, "topic": "Particle physics", "level": "noob|beginner|intermediate|advanced|expert|mastery",
 "focus": "", "length": "short|standard|full",   // 5, 8 or 12 chapters
 "code": "PHY 301",                               // 3-letter dept code + level number (050,101,201,301,501,601)
 "title": "Book title: subtitle", "department": "Department of ...",
 "description": "3-4 sentences: who it is for and what it does.",
 "prerequisites": ["..."], "objectives": ["6-8 measurable outcomes"], "hours": 40,
 "chapters": [ { "title": "...", "summary": "one sentence", "challenge": "end-of-chapter challenge",
                 "sections": [ { "title": "...", "summary": "one sentence" } ] } ],   // 3-4 sections each
 "written": {}, "createdAt": 1791700000000, "createdBy": null,
 "color": "#xxxxxx",                              // deep cloth color; white text must read on it
 "persona": "professor", "engine": "default",
 "preface": "2-4 short paragraphs in Dr. Professor's voice: who this is for, how the book works, the running examples.",
 "coverSvg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 400 400\">...</svg>", // white line art, no text, no fill backgrounds
 "bible": {
   "teacher": "how Dr. Professor teaches THIS subject (whose methods, what evidence)",
   "promise": "what the reader can do by the last page",
   "threads": ["3-5 ideas that run through every chapter"],
   "runningExamples": [ { "name": "...", "use": "..." } ],
   "conventions": ["house rules for terms, units, names, citations"],
   "canon": [ { "cite": "Author, A. (Year). Title (edition). Publisher.", "role": "what the course takes from it" } ],
   "care": "optional: how to handle disputed, sensitive or unsafe parts of the subject"
 },
 "prov": { "note": "Course plan written in Claude Code by Claude research agents, October 2026; canon editions verified by web search.", "requester": "John", "v": "dp-0.5" }
}
```

Rules
- The canon is the set of standard, respected books the course follows (5-8). Every entry must be a real
  edition verified by search (author, year, edition, publisher). Prefer the field's recognized textbooks
  and primary sources over popular books; mark practitioner or popular books as such in `role`.
- Accuracy over the requested framing. A topic built on a false premise is taught as what is true about
  it: the claims, where they came from, and what the evidence shows (stated plainly and fairly, without
  mockery). Say so in `description` and `bible.care`.
- Religion: present each tradition's teaching accurately in its own terms and sources, and keep it
  distinct from historical scholarship; respectful, never preachy or dismissive.
- Safety: anything that could hurt the reader (wild mushrooms, food safety, money) states the safe rule
  plainly in `bible.care` and the relevant chapter summaries.
