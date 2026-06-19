---
name: article
description: Build reproducible research packages for personal blog articles. Use when the user calls \article with a topic, asks to use the article skill, or wants sourced data, light statistical/econometric analysis, findings, and an article-ready outline for a blog post.
---

# Article

## Workflow

1. Parse the topic and any user-provided exploratory sources.
2. Create one package with `skills/article/scripts/new_article.py "<topic>"` from the repo root.
3. Read `references/source-policy.md`, `references/analysis-policy.md`, and `references/package-contract.md`.
4. Source trusted API or official statistical data first. Use exploratory sources only when logged.
5. Spawn `data-scout` first when tool-driven subagents are available. Load `references/subagents/data-scout.md` and pass the topic, package path, user-provided sources, source policy, and today's date. Wait for its result before download or analysis.
6. Spawn `data-downloader` next when raw data should be fetched. Load `references/subagents/data-downloader.md` and pass the package path, `sources/source-log.md`, any credential names available in the environment, and today's date. Wait for its result before analysis.
7. Then use the remaining subagents when available:
   - `analysis-checker`: load `references/subagents/analysis-checker.md`; check data, methods, and claims before writing findings.
   - `editor-outline`: load `references/subagents/editor-outline.md`; turn findings into `writing/outline.md`.
8. If subagents are unavailable, do those phases sequentially and record the fallback in `article.yaml`.
9. Keep the package reproducible: raw data or retrieval notes, processed data, runnable `analysis/analysis.py`, outputs, findings, outline, and notes.
10. Run `scripts/check_package.py <article-package>`.
11. Commit the completed package and push. If no remote exists, commit locally if possible and report `blocked: no git remote configured`.

## Package Rules

- Write only one active package per call under `articles/YYYY-MM-DD-topic-slug/`.
- Do not draft the final two-page article in v1. Produce research notes and an article-ready outline.
- Preserve raw data unless license or API terms forbid it. If raw data cannot be stored, write retrieval metadata and the reason in `sources/source-log.md`.
- Move deprecated experiments, abandoned packages, and sandbox code to `archive/YYYY-MM-DD-short-reason/`.
- Put shared code in `tools/` only after at least two packages need the same helper.

## Scripts

- `skills/article/scripts/new_article.py "<topic>"`: create the article package skeleton.
- `skills/article/scripts/check_package.py <path>`: fail if required files or directories are missing.

## Subagent Specs

- `references/subagents/data-scout.md`: data acquisition contract and source logging.
- `references/subagents/data-downloader.md`: raw data download and retrieval notes.
- `references/subagents/analysis-checker.md`: method and claim sanity check.
- `references/subagents/editor-outline.md`: article outline and notes pass.
