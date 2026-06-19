# AGENTS.md

## Project Rule

This repo produces reproducible research packages for personal blog articles. Keep it boring, clear, and small.

## Article Skill

When the user calls `\article <topic>` or asks to use the article skill:

1. Use `skills/article/SKILL.md`.
2. Create exactly one package under `articles/YYYY-MM-DD-topic-slug/`.
3. Prefer trusted public APIs and official statistical sources.
4. Use exploratory or user-provided sources only when recorded in `sources/source-log.md`.
5. Do light statistics or econometrics only when the data supports it. Do not fake precision.
6. Produce:
   - `article.yaml`
   - `sources/source-log.md`
   - reproducible raw/processed data or retrieval notes
   - runnable analysis code
   - figures/tables where useful
   - `outputs/findings.md`
   - `writing/outline.md`
   - `writing/notes.md`

## Subagents

Use tool-driven subagents when available:

- `data-scout`: find and document sources.
- `analysis-checker`: sanity-check data, methods, and claims.
- `editor-outline`: turn findings into a blog-ready outline.

If subagents are unavailable, perform the same phases sequentially and record the fallback in `article.yaml`.

## Git Hygiene

After every completed article-skill run:

1. Run the package check.
2. Review `git status`.
3. Commit only the relevant package and intentional project changes.
4. Push to the configured remote.

If no remote exists, commit locally if possible and report: `blocked: no git remote configured`.

## Clean Repo Rules

- Active article work lives only in `articles/`.
- Deprecated or sandbox work moves to `archive/YYYY-MM-DD-short-reason/`.
- Shared code goes in `tools/` only after repeated use proves it is needed.
- Do not add dependencies unless stdlib or existing tools cannot do the job.
- Do not create extra READMEs, templates, or abstractions for later.
