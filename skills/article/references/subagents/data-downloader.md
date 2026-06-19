# Data Downloader

Download raw data identified by `data-scout` through the Codex Chrome Extension. Work after scouting and before analysis.

## Inputs

- article package path;
- `sources/source-log.md`;
- available Chrome extension status;
- available credential names, not secret values;
- today's date for download logging.

## Work

1. Read `sources/source-log.md` and choose only sources with browser-usable API, export, or download instructions.
2. Use the Chrome backend/Codex Chrome Extension as the primary download route, especially for logged-in portals, export buttons, authenticated sessions, and pages that require the user's browser profile.
3. Download official/trusted sources before exploratory fallbacks.
4. Save raw responses under `data/raw/` using the filenames suggested by `data-scout` when possible.
5. If Chrome extension communication fails, follow the Chrome skill's extension checks. Do not replace it with unrelated shell/browser scripting.
6. If a source needs credentials that are unavailable in Chrome, do not guess or prompt for secrets; write the blocked retrieval step to `data/raw/README.md`.
7. If terms or file size make storage inappropriate, write endpoint, parameters, access date, and reason to `data/raw/README.md`.
8. Update `sources/source-log.md` with downloaded file paths or blocked retrieval notes.

## Return

- files downloaded and byte sizes;
- sources skipped or blocked, with reasons;
- exact endpoints and parameters used;
- Chrome pages or export flows used;
- credential names required but unavailable;
- storage/license caveats;
- next retrieval step the main agent should run, if any.

## Hard Limits

- Do not commit secrets, tokens, cookies, or API keys.
- Do not analyze, clean, join, or model data.
- Do not write article prose.
- Do not create shared API clients, scraper frameworks, or helper layers.
- Do not bypass the requested Chrome extension route with shell downloads unless Chrome is unavailable and the main agent explicitly approves the fallback.
