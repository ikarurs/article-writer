# Source Log

Access date for scouting: 2026-06-19

Topic: impact of Bundestag discussions on inflation

## Preferred Sources

### 1. Deutscher Bundestag Open Data / DIP API: plenary protocols

- Trust/order: official parliamentary source; preferred source for Bundestag discussion text and metadata.
- Access URLs:
  - Open data landing page: https://www.bundestag.de/services/opendata
  - DIP API help: https://dip.bundestag.de/%C3%BCber-dip/hilfe/api
  - API base: https://search.dip.bundestag.de/api/v1
  - Plenary metadata endpoint: `GET /plenarprotokoll`
  - Plenary full-text endpoint: `GET /plenarprotokoll-text`
  - Single-record endpoints: `GET /plenarprotokoll/{id}` and `GET /plenarprotokoll-text/{id}`
- Parameters to use: `apikey=<DIP key>`; page through list endpoints with the API pagination fields; filter by legislative period/date if available in the current OpenAPI schema; otherwise retrieve metadata and filter locally by sitting date. Use full-text endpoint only after collecting IDs from metadata.
- Geography/scope: German Bundestag plenary sittings, Germany, federal parliament.
- Date range/frequency: protocols since the 1st electoral term; new final minutes usually appear after sittings. For article work, use a reproducible fixed cutoff rather than "latest".
- Variables/units: sitting date, electoral term, protocol number, document ID, agenda/item metadata where available, speech/protocol text, speaker metadata where available. Units are documents, sittings, speeches/text segments depending on endpoint.
- License/storage notes: official parliamentary materials/open data; Bundestag states machine-readable XML/JSON data can be used for machine processing. Store retrieved JSON/XML raw responses if API terms and key conditions allow; do not commit private API keys.
- Suggested raw filenames:
  - `data/raw/bundestag_dip_plenarprotokoll_metadata_YYYYMMDD.jsonl`
  - `data/raw/bundestag_dip_plenarprotokoll_text_YYYYMMDD.jsonl`
- Suggested processed filenames:
  - `data/processed/bundestag_plenary_protocols.parquet`
  - `data/processed/bundestag_inflation_mentions_by_sitting.csv`
- Caveats/missing-data risks: API requires a key; current unauthenticated test returned HTTP 401. Recent records may lag final publication. XML structure and speaker segmentation vary across electoral periods. Search/mention counts should be treated as discussion intensity, not as evidence of effects.

### 2. Destatis GENESIS-Online: national CPI for Germany

- Trust/order: official German statistical office; preferred source for national CPI/inflation.
- Access URLs:
  - API/web service info: https://www.destatis.de/EN/Service/OpenData/api-webservice.html
  - Table page: https://www-genesis.destatis.de/datenbank/online/table/61111-0002
  - API base documented by Destatis: `https://www-genesis.destatis.de/genesisWS/rest/2020/`
  - Recommended table endpoint pattern: `data/tablefile?username=<user>&password=<password>&name=61111-0002&area=all&format=ffcsv&compress=false`
- Parameters to use: table `61111-0002`; area `all`; flat-file CSV where possible; monthly Germany values. Credentials may be required by the current API route even where public web access is free.
- Geography/scope: Germany.
- Date range/frequency: monthly table, available from 1991 onward according to the current table page.
- Variables/units: consumer price index, Germany; index base 2020=100; percent change on previous month; percent change on same month of previous year.
- License/storage notes: Destatis states GENESIS-Online is free of charge and usable under Data Licence Germany - Attribution - Version 2.0. Store raw CSV response and cite Destatis.
- Suggested raw filename: `data/raw/destatis_genesis_61111_0002_cpi_monthly_2026-06-19.csv`
- Suggested processed filename: `data/processed/germany_cpi_monthly.csv`
- Caveats/missing-data risks: API behavior changed with the new GENESIS interface; local unauthenticated test returned the web app shell rather than data. Use a registered GENESIS account or manual flat-file export if the API route does not return CSV. CPI revisions and base-year changes must be logged.

### 3. ECB Data Portal / Eurostat HICP: Germany harmonised inflation

- Trust/order: official European central-bank/statistical dissemination of Eurostat HICP; useful cross-check or alternate inflation series.
- Access URLs:
  - Data portal series page: https://data.ecb.europa.eu/data/datasets/HICP/HICP.M.DE.N.000000.4D0.ANR
  - CSV API: https://data-api.ecb.europa.eu/service/data/HICP/M.DE.N.000000.4D0.ANR?startPeriod=1996-12&format=csvdata
- Parameters to use: dataset `HICP`; key `M.DE.N.000000.4D0.ANR`; `startPeriod=1996-12`; `format=csvdata`.
- Geography/scope: Germany, harmonised index of consumer prices.
- Date range/frequency: monthly, December 1996 through latest published month; current scout retrieval reached May 2026.
- Variables/units: annual rate of change for HICP total; unit `PCCH` (percentage change); neither seasonally nor working-day adjusted.
- License/storage notes: ECB Data Portal public API; underlying source is Eurostat. Store CSV raw response with access date and preserve metadata columns.
- Suggested raw filename: `data/raw/ecb_hicp_de_total_annual_rate_monthly_2026-06-19.csv`
- Suggested processed filename: `data/processed/germany_hicp_monthly.csv`
- Caveats/missing-data risks: HICP is not identical to the national CPI; use explicitly as harmonised inflation, not as a silent substitute. The old ECB `ICP` dataset was discontinued/replaced in February 2026; use `HICP`, not `ICP`.

### 4. CPP-BT on Zenodo: derived Bundestag plenary corpus

- Trust/order: auditable derived corpus from Bundestag Open Data/DIP; preferred fallback when official API access or parsing cost blocks direct acquisition.
- Access URLs:
  - Record page: https://zenodo.org/records/15462956
  - API metadata: https://zenodo.org/api/records/15462956
  - CSV speeches download: https://zenodo.org/api/records/15462956/files/CPP-BT_2025-05-24_DE_CSV_Reden_Gesamt.zip/content
  - Speech metadata download: https://zenodo.org/api/records/15462956/files/CPP-BT_2025-05-24_DE_CSV_Reden_Metadaten.zip/content
  - XML archive download: https://zenodo.org/api/records/15462956/files/CPP-BT_2025-05-24_DE_XML_Datensatz.zip/content
- Parameters to use: fixed Zenodo record/version `15462956`, version `2025-05-24`; choose CSV speeches for quantitative counts or XML for close parsing.
- Geography/scope: German Bundestag plenary protocols.
- Date range/frequency: 1949-2025, electoral terms 1-21, snapshot as of 2025-05-24.
- Variables/units: up to 35 CSV variables; individual speeches with speaker name, party/group and office metadata from the 18th electoral term onward; protocol/date metadata; text.
- License/storage notes: CC0 1.0; record states official protocols are public-domain official works under German copyright law. Files are large; store only needed raw archives or retrieval notes if storage is constrained.
- Suggested raw filenames:
  - `data/raw/cpp_bt_2025-05-24_speeches.zip`
  - `data/raw/cpp_bt_2025-05-24_speech_metadata.zip`
- Suggested processed filename: `data/processed/cpp_bt_inflation_mentions_by_sitting.csv`
- Caveats/missing-data risks: not an official Bundestag publication; snapshot stops at 2025-05-24 and will miss later sittings unless updated via pipeline/API. Derived segmentation may encode parser assumptions; consult codebook before using speaker-level fields.

## Rejected Or Lower-Priority Sources

- Open Discourse: useful structured Bundestag speeches, but exploratory/derived and less directly auditable than Bundestag Open Data/DIP or CPP-BT for this package.
- FRED Germany CPI/HICP series: convenient mirror, but lower priority than Destatis/ECB/Eurostat because it adds another redistribution layer and may lag/source-map differently.
- IMF CPI dataset: official international source, but broader than needed and less direct for Germany than Destatis national CPI.
- Bundesbank legacy time-series database: official and useful context, but the old time-series database is scheduled to be shut down on 2026-06-30; prefer Destatis for national CPI and ECB Data Portal for HICP API stability.
- News articles/press releases about inflation: useful for context only, not preferred as time-series data.
