# Dr. Professor

A full course on any subject, at any level, from Noob to Mastery: a textbook and workbook in one, with lectures, figures, practice problems, quizzes, graded challenge exercises, office hours, a final exam and a certificate.

- **Plan and brainstorm:** [`docs/PLAN.md`](docs/PLAN.md)
- **Prototype:** [`app/dr-professor.html`](app/dr-professor.html), a single-file app published as a private Claude artifact. It uses the artifact `sample` capability (Claude writes the courses), `db` (shared course library, private progress), `user` and `downloads`. Opened outside Claude, it runs read-only on browser storage, and course writing is disabled.
- **Seed library:** `app/seed/` holds four course syllabi (Birds, Game Design, Outer Space, Energy and Power) and a hand-written Chapter 1 of *ORN 101 Birds* with three figures. Run `python3 scripts/build_seed.py` to assemble the documents in `app/seed/dist/`; these are what get written to the artifact database.
