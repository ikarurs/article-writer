# Raw Data Retrieval Notes

Access date for scouting: 2026-06-19
Download attempt date: 2026-06-19
Route-aware download date: 2026-06-23

The first Chrome-backed retrieval pass saved no raw data because direct API navigations and page-context retries were blocked by Chrome-side UI/extension failures. A later route-aware pass saved public API files without Chrome where browser state was unnecessary.

## Raw Files Saved

- `ecb_hicp_de_total_annual_rate_monthly_2026-06-23.csv`
  - Source: `https://data-api.ecb.europa.eu/service/data/HICP/M.DE.N.000000.4D0.ANR?startPeriod=1996-12&format=csvdata`
  - Size: 108203 bytes
  - SHA-256: `4afb861b366a162562238b18387582bf1b8e825d246f98d1d5c7cd58187d9bdd`
- `zenodo_cpp_bt_record_15462956_2026-06-23.json`
  - Source: `https://zenodo.org/api/records/15462956`
  - Size: 18027 bytes
  - SHA-256: `8a61abefe807533b192105d44ccd3fc02a67a4b96f003b05416a379bb2a19c60`

## Still Blocked Or Deferred

- DIP API: requires `apikey=<DIP key>`; no key was available, and no raw response was saved.
- Destatis GENESIS `61111-0002`: guest endpoint returned an HTML app shell rather than CSV; use a GENESIS account or browser export.
- CPP-BT corpus ZIPs: not downloaded yet because the speech archive is large; Zenodo metadata is saved so the exact file URLs and sizes are reproducible.

## Chrome Retrieval Attempt Log

1. Bundestag/DIP plenary metadata
   - Attempted URL: `https://search.dip.bundestag.de/api/v1/plenarprotokoll`
   - Parameters: none; this was a no-key availability check before any keyed retrieval.
   - Intended output: `bundestag_dip_plenarprotokoll_metadata_20260619.jsonl`
   - Result: blocked. Chrome reported `net::ERR_BLOCKED_BY_CLIENT`.
   - Next retrieval step: retry through Chrome after dismissing the blocking Chrome/extension UI, with `apikey=<DIP key>` if a DIP API key is available in the user's browser/session. Do not store the key.

2. ECB Data Portal HICP Germany annual rate
   - Attempted URL: `https://data-api.ecb.europa.eu/service/data/HICP/M.DE.N.000000.4D0.ANR?startPeriod=1996-12&format=csvdata`
   - Parameters: dataset `HICP`; key `M.DE.N.000000.4D0.ANR`; `startPeriod=1996-12`; `format=csvdata`.
   - Intended output: `ecb_hicp_de_total_annual_rate_monthly_2026-06-19.csv`
   - Result: blocked. Direct Chrome navigation reported `net::ERR_BLOCKED_BY_CLIENT`; retry from the ECB Data Portal page was blocked by Chrome with `another extension UI is open on this page`.
   - Next retrieval step: retry through Chrome once the extension UI is dismissed. This source should not require credentials.

3. Destatis GENESIS national CPI table 61111-0002
   - Attempted URL: `https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile?username=GAST&password=GAST&name=61111-0002&area=all&format=ffcsv&compress=false`
   - Parameters: table `61111-0002`; area `all`; flat-file CSV; uncompressed; public `GAST` check only.
   - Intended output: `destatis_genesis_61111_0002_cpi_monthly_2026-06-19.csv`
   - Result: blocked. Chrome reported `another extension UI is open on this page` during direct navigation and during retry from the GENESIS table page.
   - Next retrieval step: retry through Chrome after dismissing the blocking UI. If `GAST` is not accepted, use an available GENESIS account in Chrome or manual table export, but do not prompt for or store credentials.

4. Zenodo CPP-BT record metadata and derived Bundestag corpus files
   - Attempted metadata URL: `https://zenodo.org/api/records/15462956`
   - Attempted from page: `https://zenodo.org/records/15462956`
   - Intended metadata output: `zenodo_cpp_bt_record_15462956_2026-06-19.json`
   - Result: blocked. Chrome reported `another extension UI is open on this page`.
   - Next retrieval step: retry metadata first through Chrome; then inspect file sizes and download only the needed archive(s), likely `CPP-BT_2025-05-24_DE_CSV_Reden_Gesamt.zip` and/or `CPP-BT_2025-05-24_DE_CSV_Reden_Metadaten.zip`, if storage is acceptable.

## Recommended Retrieval Order

1. Bundestag/DIP plenary protocols
   - Use `https://search.dip.bundestag.de/api/v1/plenarprotokoll` for metadata and `https://search.dip.bundestag.de/api/v1/plenarprotokoll-text` for full text.
   - Include `apikey=<DIP key>` and keep the key out of committed files.
   - Save raw responses as JSONL:
     - `bundestag_dip_plenarprotokoll_metadata_YYYYMMDD.jsonl`
     - `bundestag_dip_plenarprotokoll_text_YYYYMMDD.jsonl`
   - If API access is unavailable, use the Bundestag Open Data page (`https://www.bundestag.de/services/opendata`) or the CPP-BT Zenodo fallback below.

2. Destatis national CPI
   - Preferred table: GENESIS `61111-0002`, "Verbraucherpreisindex: Deutschland, Monate".
   - API pattern: `https://www-genesis.destatis.de/genesisWS/rest/2020/data/tablefile?username=<user>&password=<password>&name=61111-0002&area=all&format=ffcsv&compress=false`
   - Save as `destatis_genesis_61111_0002_cpi_monthly_2026-06-19.csv`.
   - If API export fails, use the GENESIS table web export and record the manual export settings.

3. ECB/Eurostat HICP cross-check
   - Use `https://data-api.ecb.europa.eu/service/data/HICP/M.DE.N.000000.4D0.ANR?startPeriod=1996-12&format=csvdata`.
   - Save as `ecb_hicp_de_total_annual_rate_monthly_2026-06-19.csv`.
   - Treat as harmonised inflation, not as an exact substitute for Destatis national CPI.

4. CPP-BT derived Bundestag corpus fallback
   - Record/API: `https://zenodo.org/api/records/15462956`.
   - Suggested downloads:
     - `https://zenodo.org/api/records/15462956/files/CPP-BT_2025-05-24_DE_CSV_Reden_Gesamt.zip/content`
     - `https://zenodo.org/api/records/15462956/files/CPP-BT_2025-05-24_DE_CSV_Reden_Metadaten.zip/content`
   - Save as:
     - `cpp_bt_2025-05-24_speeches.zip`
     - `cpp_bt_2025-05-24_speech_metadata.zip`
   - Use only with its codebook and note that the snapshot ends on 2025-05-24.
