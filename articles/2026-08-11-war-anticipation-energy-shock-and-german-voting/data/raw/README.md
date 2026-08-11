# Raw Data Retrieval Log

Access date: 2026-08-11

Files below were fetched unchanged with `skills/article/scripts/download_url.py <url> <output>`. The script performed direct HTTP GET requests with redirects enabled and its 60-second default timeout. No query parameters, custom headers, browser exports, credentials, cookies, or secrets were used.

## Downloaded

| File | Source URL | Bytes | SHA-256 | Check |
|---|---|---:|---|---|
| `elections/btw21_wbz.zip` | https://www.bundeswahlleiterin.de/dam/jcr/c2cd99e6-064e-4ebc-b634-f86b5c0e14b3/btw21_wbz.zip | 6,155,988 | `ccdceeb7d210c35eebdd4e297399f36e6e5afa8569eaaf45e90b489faa068726` | ZIP opened; 6 entries |
| `elections/ew24_wbz.zip` | https://bundeswahlleiterin.de/dam/jcr/8d0e36e7-d9d2-400b-80f8-1e2005983971/ew24_wbz.zip | 4,193,564 | `ac926f430b586ef097aaae12221edb74df9a98110e96d7c0a8a2a2e78bf57608` | ZIP opened; 6 entries |
| `elections/btw25_wbz.zip` | https://bundeswahlleiterin.de/dam/jcr/e79a7bd3-0607-4e87-9752-8e601e299e00/btw25_wbz.zip | 6,059,110 | `faedc8af49617131af59af9edeb38c17a166bea5c3badfc7ed566e4d49c7e516` | ZIP opened; 6 entries |
| `context/p_wsi_report_92_2023.pdf` | https://www.boeckler.de/fpdf/HBS-008748/p_wsi_report_92_2023.pdf | 1,776,340 | `85400ea16cac47a333be48630e47995dea6693654163ac817e0240144ac46517` | `%PDF-` header verified |
| `context/wsi_report_92e_2023.pdf` | https://www.wsi.de/fpdf/HBS-008835/p_wsi_report_92e_2023.pdf | 1,951,781 | `19dfff6fc47b82ca21481585403ab2c9a55e78760a5c3afec6bdae202a743670` | `%PDF-` header verified; English edition supplied by user |
| `context/cesifo1_wp12887.pdf` | https://www.ifo.de/DocDL/cesifo1_wp12887.pdf | 3,905,534 | `29198cdc6cdec0b7755b59db4d0dde84758e583205d5a52e3b11b149ac6dc40c` | 104-page PDF; abstract page rendered and inspected |
| `elections/state/ni_landtag_2017.csv` | https://wahlen.statistik.niedersachsen.de/LW2017/wahlergebnis.csv | 12,430 | `98a6cf9dceb95b0f30a545c62bc2ed7528109b58e647ea7dd80d7d6c7c6f2c2e` | UTF-8 semicolon CSV; 87 unique constituencies |
| `elections/state/ni_landtag_2022.csv` | https://wahlen.statistik.niedersachsen.de/LW2022/wahlergebnis.csv | 14,094 | `25316d1de8a18980080de7473e998ba2e8ca76e611e870445da53944ed34ee1b` | UTF-8 semicolon CSV; 87 unique constituencies |
| `elections/state/berlin_agh_2021_2023.xlsx` | https://wahlen-berlin.de/wahlen/BE2023/AFSPRAES/agh/DL/DL_BE_AGHBVV2023.xlsx | 2,772,628 | `66cef4c0180b42a8de7ba683579545bd989b51b597c274a6d3a481002ddc2caa` | XLSX opened; `AGH_W2` has 3,764 result rows |
| `elections/state/sh_ltw_2017_precinct.csv` | https://www.statistik-nord.de/fileadmin/wahl/LTWSH-2017/ergebnis-download.csv | 350,134 | `b58d61bbee98092bee77a89f605a72f88940af1ca97cd3be5ff6459f5bea3c5b` | Official precinct results |
| `elections/state/sh_ltw_2022_precinct.csv` | https://www.statistik-nord.de/fileadmin/wahlen/sh/ltw22/ergebnis-download.csv | 446,076 | `b3b7bbf2780493a0788ce0abf845cb8179c2034fddc80069c1b9e79ba4aa902c` | Official precinct results and municipality keys |
| `elections/state/sh_kommunal_2023_precinct.csv` | https://www.wahlen-sh.de/grw/ergebnis-download-gemeindewahl.csv | 333,488 | `a3f68d2b1ddd7989125ceecd54a3395ca98a189274f66f9cc16ebbe4a5c26a3a` | Official municipality/local-election results |
| `elections/state/sh_kommunal_2018_municipality.xlsx` | https://www.statistik-nord.de/fileadmin/Dokumente/Wahlen/Schleswig-Holstein/Kommunalwahlen/2018/Endg%C3%BCltige_Ergebnisse_Gemeindewahlen_SH_2018.xlsx | 7,507,141 | `b83c4df1cb0e4af546b7bacfafb52600e4c11abdcda9f2b1104f305be3201d5e` | Official municipality workbook |
| `elections/state/sh_municipalities_2022.zip` | https://www.statistik-nord.de/fileadmin/Dokumente/Wahlen/Schleswig-Holstein/Landtagswahlen/2022/Vor_der_Wahl/Gemeinden.zip | 1,872,502 | `70d1e5347a56bfc40e196878c013509a6b3983a24632a53e255769c07f97862b` | Nested GeoJSON; 1,106 features; EPSG:25832 |
| `elections/state/bb_ltw_2019_aggregates.xlsx` | https://wahlergebnisse.brandenburg.de/wahlen/publikationen/dowmies/DL_BB_2_LT2019.xlsx | 318,937 | `3cf66b1d4345bbe7d64806e658925739a2b51c34fab12fe3f4e45f21d0480c9e` | Official municipality aggregates |
| `elections/state/bb_ltw_2024_aggregates.xlsx` | https://download.statistik-berlin-brandenburg.de/24337cfdd3a6b8a6/ae7033fb6270/DL_BB_2_LT2024.xlsx | 380,106 | `a522dd67f31645c4f8f0a5e413f2bcd3cf493e589ccb59734afcec11afc528e9` | Official municipality aggregates |
| `spatial/brandenburg_bbox_vg250.geojson` | BKG VG250 WFS `vg250_gem`, EPSG:4326, bbox 11.2,51.3,14.8,53.6 | 5,102,487 | `cf832ae820a13cd00050567b4f26adbda2447a20b14851b3ee7781accf743166` | 1,023 bbox features; analysis filters `sn_l=12` |
| `spatial/prtr_2024.zip` | https://thru.de/wp-content/uploads/2026/03/prtr_2024.zip | 11,050,284 | `50474d9e8c7e3f92a49c960b32176b0195cdaf65197f4b93114cd8525e2c5206` | UBA PRTR SQLite archive; PCK coordinate queried from refinery records |

The official election ZIPs contain the original result CSV, municipality-key/guide CSV, data descriptions, notes, and imprint files. They remain unextracted so the raw downloads stay immutable. Review each archive's bundled imprint and notices before redistribution.

The WSI and CESifo papers are public documentation but copyright-protected. Keep them for research reference and citation; do not treat the WSI report as respondent microdata or redistribute either paper outside the applicable terms. The Berlin filename is retained for package stability, but the workbook itself contains 2023 results only.

## Blocked or intentionally not downloaded

### GLES microdata

- Catalogue: https://www.gesis.org/en/gles/data-and-documentation
- Requested scope: Tracking T51–T59 and, if needed, Panel Waves 22–28, including the dataset-specific questionnaires, codebooks, citations, versions, and licenses.
- Classification: `credentialed_api` / authenticated browser download.
- Status: Blocked because GESIS requires one-time account login and no relevant credential name or existing authenticated session was available.
- Next step: A user with a GESIS account should download the documented dataset versions and accompanying files, then record filenames, versions, byte sizes, SHA-256 hashes, and dataset-specific redistribution terms here. Do not place credentials in code or logs.

### Tankerkönig historical MTS-K archive

- Documentation: https://creativecommons.tankerkoenig.de/?menu=false
- Onboarding: https://onboarding.tankerkoenig.de/
- Requested scope: Historical station metadata and daily price-change files for 2021-01-01 through 2024-12-31.
- Classification: `credentialed_api` and potentially `too_large_or_restricted` for repository storage.
- Status: Blocked because the historical git archive requires a registered, verified account accepting its terms; no relevant credential or existing session was available. The live Tankerkönig API was not used.
- Next step: Complete onboarding, review the accepted BY-NC-SA-4.0 and transfer restrictions, and clone only if package storage is permitted. Otherwise record repository URL, commit IDs, retrieval date/range, hashes, and the restriction without copying raw files into this package.

### WSI respondent microdata

- Access page: https://www.wsi.de/de/datenzentrum-methodik-und-datenzugang-erwerbspersonenbefragung-32071.htm
- Classification: `too_large_or_restricted`.
- Status: Not downloadable. WSI states that the HBS-Erwerbspersonenbefragung respondent data are not currently offered to the scientific public. Only the published report was retrieved.

### Literature manuscript

- Metadata: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6542238
- Classification: contextual source.
- Status: Metadata only. The manuscript was not downloaded because it is unnecessary for the raw-data stage and its displayed download terms should be checked first.

## Spatial processing notes

The Schleswig-Holstein Landtag panel matches stable polling-district identifiers and then aggregates them to 1,097 municipality units; it covers 94.00% of the 2017 electorate rather than pretending unmatched districts are observed. The local-election panel matches 1,074 municipalities, but party comparisons require candidature in both years. The Brandenburg panel matches 409 municipality keys across 2019 and 2024; four changed keys are excluded. Geometry is used only for mapping and representative-point distance. PCK Schwedt is identified in PRTR at longitude 14.23812, latitude 53.08759. Distance is not a measured fuel-price shock.

The BKG DLM250 2022 pipeline archive was inspected as a possible source but not downloaded: the archive is about 311 MB and its product attributes may not establish supply direction or Russian-oil dependence. It remains a deferred contextual source, not exposure data.
