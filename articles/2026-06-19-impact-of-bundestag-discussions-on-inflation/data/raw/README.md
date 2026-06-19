# Raw Data Retrieval Notes

Access date for scouting: 2026-06-19

No raw data files were downloaded in this scouting pass because the user requested edits only to `sources/source-log.md` and this retrieval-notes file.

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
