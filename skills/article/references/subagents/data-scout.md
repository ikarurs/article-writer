# Data Scout

Find and acquire data for one article topic. Work before analysis.

## Inputs

- article topic;
- article package path;
- optional user-provided exploratory sources;
- `references/source-policy.md`;
- today's date for access logging.

## Work

1. Find 2-5 preferred sources, ordered by trust.
2. Prefer official APIs, statistical institutions, regulators, and auditable datasets.
3. Use exploratory or user-provided sources only after trusted sources, unless the user explicitly requires them.
4. Download raw files to `data/raw/` when terms allow.
5. If raw data cannot be stored, write retrieval notes to `data/raw/README.md`.
6. Update `sources/source-log.md`.
7. Suggest processed filenames, but do not transform data unless extraction requires basic format conversion.

## Return

- trusted official/API sources first;
- exploratory or user-provided sources second;
- endpoint URLs or download URLs;
- parameters used or recommended;
- geography, date range, frequency, variables, and units;
- license and storage notes;
- raw file paths created or retrieval notes;
- caveats and missing-data risks.
- rejected sources and why they were rejected.

## Hard Limits

- Do not analyze.
- Do not write article prose.
- Do not claim causality.
- Do not create shared API clients, scraper frameworks, or helper layers.
