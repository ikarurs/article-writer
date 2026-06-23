# Data Downloader

Download raw data identified by `data-scout`. Work after scouting and before analysis.

## Inputs

- article package path;
- `sources/source-log.md`;
- available Chrome extension status;
- available credential names, not secret values;
- today's date for download logging.

## Work

1. Read `sources/source-log.md` and classify each source:
   - `public_api`: direct public API/download URL.
   - `browser_export`: export button or page flow needing Chrome.
   - `credentialed_api`: API requiring a key/account/session.
   - `too_large_or_restricted`: storage is too large or not allowed.
2. For `public_api`, run `skills/article/scripts/download_url.py <url> <output>` and save under `data/raw/`.
3. For `browser_export`, use the Chrome backend/Codex Chrome Extension.
4. For `credentialed_api`, use only available credential names or an existing Chrome session. Do not ask for or store secret values.
5. For `too_large_or_restricted`, write endpoint, parameters, access date, and reason to `data/raw/README.md`.
6. Download official/trusted sources before exploratory fallbacks.
7. Update `sources/source-log.md` with downloaded file paths, byte sizes, checksums, or blocked notes.

## Return

- files downloaded and byte sizes;
- SHA-256 checksums for downloaded files;
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
- Do not use Chrome for direct public API URLs unless stdlib download fails for a reason Chrome can plausibly fix.
