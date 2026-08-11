# Source Log

Topic: War, anticipation, energy shock, and German voting  
Accessed: 2026-08-11

Sources are ordered by trust and usefulness. No substantive raw data were downloaded during the data-scout pass.

## 1. German Longitudinal Election Study (GLES), GESIS

- **Role:** Main repeated political-sentiment source around the invasion and subsequent energy crisis.
- **Publisher:** GESIS – Leibniz Institute for the Social Sciences / GLES.
- **Catalogue:** https://www.gesis.org/en/gles/data-and-documentation
- **Access:** One-time GESIS registration is required: https://login.gesis.org/ . Dataset pages, questionnaires, detailed study descriptions, version numbers, licenses, and downloads are linked from the catalogue. Preserve each downloaded dataset's license and citation file; do not redistribute microdata unless its dataset-specific terms permit it.
- **Downloader status (2026-08-11):** Blocked. No relevant credential or existing authenticated session was available, and the one-time login cannot be automated without user credentials. No GLES microdata or documentation bundle was downloaded and no secret was requested or stored.
- **Priority repeated cross-sections (GLES Tracking):** T51, ZA7709, 2022-02-03–2022-02-14; T52, ZA7710, 2022-06-02–2022-06-09; T53, ZA7711, 2022-10-13–2022-10-21; T54, ZA7712, 2023-04-17–2023-04-21; T55, ZA7713, 2023-08-07–2023-08-14; T56, ZA7714, 2023-11-08–2023-11-15; T57, ZA7715, 2024-03-06–2024-03-15; T58, ZA7716, 2024-06-12–2024-07-02; T59, ZA10002, 2024-10-09–2024-10-17. Cumulation through 2023: ZA6832.
- **Priority panel waves:** Wave 22, ZA7728, 2022-05-18–2022-05-31; Wave 23, ZA7729, 2022-10-12–2022-10-25; Wave 24, ZA7730, 2023-05-03–2023-05-16; Wave 25, ZA7731, 2023-10-11–2023-10-24; Waves 26–27, ZA7732, 2024-06-12–2024-06-25 and 2024-09-24–2024-10-08; Wave 28, ZA10117, 2024-12-11–2024-12-22.
- **Geography/frequency:** Germany; individual respondents; roughly quarterly tracking waves and irregular panel waves. Public files generally support national and broad regional analysis, not a municipality panel.
- **Candidate variables:** survey/wave and field dates; Sunday-question vote intention; party identification and propensities; retrospective vote; government, democracy, party, and politician evaluations; economic expectations; issue salience; war/Ukraine or energy items when present; Bundesland or East/West; town size; demographics; design and analysis weights. Confirm exact wording and availability in every questionnaire before harmonising.
- **Join keys:** Wave/study identifiers and interview dates join to national daily or monthly energy-price series. Stable respondent identifiers join panel waves subject to the supplied documentation. Fine geographic linkage is not assumed.
- **Caveats:** T51 ended ten days before 2022-02-24 and is the closest clean pre-invasion tracking wave. T52 is already post-invasion. Question modules and samples change across waves; missing variables must not be coded as substantive responses. The catalogue's sensitive regional file ZA6828 covers 2013–2021, not the post-invasion period. Survey evidence identifies timing and associations unless a defensible design establishes more.

## 2. Official German election calendar and granular results

- **Role:** Fix event dates and provide actual voting outcomes for validation or a separate aggregate design.
- **Publisher:** Die Bundeswahlleiterin; polling-district files are a joint publication of federal and Land returning officers.
- **Past-election calendar:** https://www.bundeswahlleiterin.de/service/wahltermine/fruehere-wahlen.html
- **Federal and European election dates:** https://www.bundeswahlleiterin.de/service/glossar/w/wahltermin.html
- **2021 Bundestag polling-district ZIP:** https://www.bundeswahlleiterin.de/dam/jcr/c2cd99e6-064e-4ebc-b634-f86b5c0e14b3/btw21_wbz.zip
- **2024 European election polling-district ZIP:** https://bundeswahlleiterin.de/dam/jcr/8d0e36e7-d9d2-400b-80f8-1e2005983971/ew24_wbz.zip
- **2025 Bundestag polling-district ZIP:** https://bundeswahlleiterin.de/dam/jcr/e79a7bd3-0607-4e87-9752-8e601e299e00/btw25_wbz.zip
- **2025 constituency open-data route:** https://www.bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata.html and CSV directory https://www.bundeswahlleiterin.de/bundestagswahlen/2025/ergebnisse/opendata/btw25/csv/
- **Geography/date/frequency:** About 85,000 polling districts in 2021, 92,000 in the 2024 European election, and 95,000 in 2025; one cross-section per election. The 2024 and 2025 ZIPs include explanatory municipality-key files at territory dates 2024-06-30 and 2024-12-31.
- **Variables:** eligible voters, voters/turnout, valid and invalid ballots, first and second votes where applicable, party/candidate vote counts, polling-district type, municipality keys, and territorial metadata as documented inside each archive.
- **Join keys:** Use the supplied Gemeindekennziffer mapping and aggregate polling districts to harmonised municipalities before joining external geography or prices. Keep election, municipality, and polling-district identifiers as strings with leading zeroes.
- **License/storage:** Official files are free downloads. Preserve original ZIPs, internal documentation, access date, checksums, and required source/copyright notices. The 2025 boundary products state Data License Germany – Attribution 2.0; verify the notice packaged with each results archive rather than applying that license automatically to every file.
- **Downloaded unchanged (2026-08-11):**
  - `data/raw/elections/btw21_wbz.zip` — 6,155,988 bytes — SHA-256 `ccdceeb7d210c35eebdd4e297399f36e6e5afa8569eaaf45e90b489faa068726` — endpoint exactly as listed above; ZIP opened successfully with 6 entries.
  - `data/raw/elections/ew24_wbz.zip` — 4,193,564 bytes — SHA-256 `ac926f430b586ef097aaae12221edb74df9a98110e96d7c0a8a2a2e78bf57608` — endpoint exactly as listed above; ZIP opened successfully with 6 entries.
  - `data/raw/elections/btw25_wbz.zip` — 6,059,110 bytes — SHA-256 `faedc8af49617131af59af9edeb38c17a166bea5c3badfc7ed566e4d49c7e516` — endpoint exactly as listed above; ZIP opened successfully with 6 entries.
- **Retrieval method/parameters:** `skills/article/scripts/download_url.py <url> <output>`; direct HTTP GET, redirect following, 60-second default timeout; no query parameters, headers, browser session, or credentials.
- **Caveats:** Polling districts and municipality boundaries change. Special/brief-vote districts may not map cleanly to residential exposure. The 2021 result incorporates a later partial repeat election in Berlin on the current results route; retain the archived 2021 main-election file above and document any Berlin treatment. Land and local-election granular files live with the respective Land returning officers; add only a selected election's official route after the analysis chooses it.

### Selected state-election files

- **Lower Saxony 2017:** https://wahlen.statistik.niedersachsen.de/LW2017/wahlergebnis.csv — `data/raw/elections/state/ni_landtag_2017.csv`, 12,430 bytes, SHA-256 `98a6cf9dceb95b0f30a545c62bc2ed7528109b58e647ea7dd80d7d6c7c6f2c2e`.
- **Lower Saxony 2022:** https://wahlen.statistik.niedersachsen.de/LW2022/wahlergebnis.csv — `data/raw/elections/state/ni_landtag_2022.csv`, 14,094 bytes, SHA-256 `25316d1de8a18980080de7473e998ba2e8ca76e611e870445da53944ed34ee1b`.
- **Berlin 2023 repeat:** https://wahlen-berlin.de/wahlen/BE2023/AFSPRAES/agh/DL/DL_BE_AGHBVV2023.xlsx — `data/raw/elections/state/berlin_agh_2021_2023.xlsx`, 2,772,628 bytes, SHA-256 `66cef4c0180b42a8de7ba683579545bd989b51b597c274a6d3a481002ddc2caa`.
- **Berlin historical aggregate series:** https://www.statistik-berlin-brandenburg.de/abgeordnetenhauswahlen-bvv-berlin/ — official rounded list-vote shares for 2021 and 2023.
- **Retrieval:** All three files were fetched unchanged on 2026-08-11 with `skills/article/scripts/download_url.py`, direct HTTP GET and no credentials. The Lower Saxony files each contain 87 unique constituency rows. The Berlin workbook's `AGH_W2` sheet contains 3,764 ordinary and postal result rows and reproduces the published 2023 Berlin party shares to rounding.
- **Berlin limitation:** Despite its local filename, the downloaded workbook contains 2023 results only. The historical 2021 granular workbook could not be recovered through a stable official download route. The v1 analysis therefore uses only the official rounded Berlin-wide 2021 shares; it does not claim polling-district matching.

## 3. MTS-K fuel-price history via Tankerkönig

- **Role:** Highest-resolution feasible German retail-energy price panel; use as the price outcome or national/municipal shock measure, not as household gas or electricity prices.
- **Origin:** All covered stations report price changes to the Bundeskartellamt's Markttransparenzstelle für Kraftstoffe (MTS-K). Tankerkönig is a licensed consumer-information service and archive distributor.
- **Documentation/history access:** https://creativecommons.tankerkoenig.de/?menu=false
- **Registration:** https://onboarding.tankerkoenig.de/ ; historical git-repository access requires a registered and verified user accepting the terms. If registration remains unavailable, contact `info@tankerkoenig.de` and record the response.
- **Downloader status (2026-08-11):** Blocked. The historical archive is authenticated and no relevant credential or existing session was available. The live API was not called. No raw fuel-price file was created.
- **Terms:** https://onboarding.tankerkoenig.de/geschaeftsbedingungen
- **Official reporting rules:** https://www.gesetze-im-internet.de/mtskraftv/BJNR059500013.html
- **Geography/date/frequency:** Station UUID with latitude, longitude, address, and postcode; all Germany; archived from June 2014 onward; one file per day containing reported price changes, updated daily.
- **Variables/units:** timestamp; station UUID; E5, E10, and diesel price in EUR/litre; station status and change bitmask; station name, brand, coordinates, and address in station metadata.
- **Retrieval parameters:** Clone or download only the authenticated historical repository documented after onboarding. Limit acquisition initially to 2021-01-01 through 2024-12-31 plus station metadata; expand only if the selected analysis needs longer pre-trends. Do not use the live radius API to reconstruct history.
- **Join keys:** Station UUID joins changes to station metadata. Coordinates or postcode can be spatially joined to municipalities; retain boundary vintage and match quality.
- **License/storage:** The live API states CC BY 4.0. The historical archive states BY-NC-SA 4.0 and the service terms restrict onward transfer. Treat the historical files as non-commercial, attribution-required, and non-redistributable until the accepted terms are reviewed. If storage in the article package is not permitted, retain only retrieval instructions, checksums, and derived aggregate outputs allowed by the terms.
- **Caveats:** History stores changes, not a complete price at every timestamp; reconstruct the prevailing price from the last valid change and calculate a time-weighted daily measure. `-1` indicates an invalid price. Station entry/exit, coordinate changes, outages, and price-report corrections require checks. Retail motor fuel is not household gas/electricity, and proximity to a pipeline or refinery does not establish a station's supply source.

## 4. Published WSI Erwerbspersonenpanel evidence and documentation

- **Role:** Published benchmark for repeated voting intention, perceived inflation/energy burdens, Ukraine attitudes, and AfD support among German labour-force participants.
- **Report:** Andreas Hövermann (2023), *Das Umfragehoch der AfD: Aktuelle Erkenntnisse aus dem WSI-Erwerbspersonenpanel*, WSI Report No. 92, November 2023: https://www.boeckler.de/fpdf/HBS-008748/p_wsi_report_92_2023.pdf
- **Panel methodology, wave questionnaires/codebooks, and access status:** https://www.wsi.de/de/datenzentrum-methodik-und-datenzugang-erwerbspersonenbefragung-32071.htm
- **Geography/date/frequency:** German labour-force participants aged 16+ in a CAWI online access panel. The report follows repeated respondents from July 2021, October 2021, January 2022, November 2022, and July 2023; panel waves 8–10 cover April/May 2022, November 2022, and 2023-06-29–2023-07-20. National and East/West reporting is feasible from published tables.
- **Published variables:** Sunday-question vote intention or actual 2021 second vote; AfD switching categories; perceived burdens and worries about inflation, energy/food prices, living standards, and personal finances; institutional trust; attitudes concerning the war and refugees; employment and demographic characteristics; weights.
- **Access/license/storage:** The report and questionnaire/codebook PDFs are public for reading and citation; observe their copyright notices. As of 2026-08-11, WSI explicitly says the respondent microdata are not offered to the scientific public and that an access concept is still being developed. Store metadata and public documentation only; do not plan a raw-data replication without written access from WSI.
- **Downloaded unchanged (2026-08-11):** `data/raw/context/p_wsi_report_92_2023.pdf` — 1,776,340 bytes — SHA-256 `85400ea16cac47a333be48630e47995dea6693654163ac817e0240144ac46517` — `%PDF-` header verified. Retrieval used `skills/article/scripts/download_url.py` with the report URL above, direct HTTP GET, no parameters, headers, browser session, or credentials.
- **Caveats:** Quota sample from a Payback online-access panel, not a probability sample; excludes retirees and students who are not in the labour force; attrition and question timing matter. The report is contextual published evidence, not an available analysis dataset and not a local geographic panel.

## 5. Closest overlapping study: Berlin energy-price exposure and voting

- **Citation metadata:** Lukas Kirchner (2026), *Inflation and Electoral Outcomes*, SSRN abstract 6542238: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6542238
- **Role:** Literature/context only. The study compares Berlin polling-district vote-share changes using predetermined local heating-technology exposure to the 2022 energy-price shock. It is the closest verified overlap with the proposed aggregate design and should be read before claiming novelty.
- **Geography/date/frequency:** Berlin polling districts; election-level changes surrounding the 2022 shock, as specified in the paper.
- **Variables:** Party vote shares and predetermined local heating-technology exposure, with exact construction to be extracted from the paper and supplements.
- **Access/license/storage:** Public SSRN metadata page. Record title, author, version date, abstract ID, and access date. Download/store the manuscript only if the displayed SSRN terms permit it; otherwise keep a citation and retrieval note.
- **Caveats:** Working paper and potentially revised after access. Do not import its estimates as data. Its Berlin setting and heating-exposure design materially narrow the article's novelty claim.

## 6. Benchmark causal study: Konc et al. (2026)

- **Citation:** Théo Konc, Jan Christoph Steckel, Jacob Edenhofer, Jens Ewald, and Thomas Sterner (2026), *The Political Consequences of Energy Price Shocks: Evidence from Germany*, CESifo Working Paper No. 12887, 31 July 2026: https://www.ifo.de/DocDL/cesifo1_wp12887.pdf
- **Downloaded unchanged:** `data/raw/context/cesifo1_wp12887.pdf` — 3,905,534 bytes — SHA-256 `29198cdc6cdec0b7755b59db4d0dde84758e583205d5a52e3b11b149ac6dc40c` — 104 pages; abstract page rendered and visually inspected.
- **Design and finding:** Four original panel waves exploit staggered supplier adjustments to household monthly electricity instalments. In the authors' later-treated difference-in-differences design, an above-median realised increase raises AfD support by 7.5 percentage points; the paper reports persistence and subsequent attitudinal adjustment.
- **Relevance:** This is the benchmark mechanism the proposed article would seek to generalise from households to places and elections. It identifies realised household electricity-payment exposure, whereas this public-data v1 observes only aggregate sentiment and election timing. Its estimate is not imported into the article's data and should not be compared mechanically with aggregate election swings.
- **Caveats:** New working paper, not peer-reviewed in this version. The identifying assumptions concern supplier billing timing and later-treated controls; external validity to motor-fuel shocks, municipality exposure, or election returns is not automatic.

## 7. Fuel-price pass-through benchmark: Gregor and Haucap (2025)

- **Citation:** Leonard Gregor and Justus Haucap (2025), *The Rise of Refinery Margins: The Case of the Energy Tax Cut in Germany*, CESifo Working Paper No. 12214: https://www.ifo.de/DocDL/cesifo1_wp12214.pdf
- **Role:** Mechanism/context. The paper studies the June-September 2022 German fuel-tax cut with wholesale pricing and quantity data, reporting incomplete pass-through and heterogeneity over time and across regions. It supports measuring realised local pump-price movements rather than assuming uniform national pass-through.
- **Caveat:** It studies a tax intervention and refinery margins, not voting, Russian-pipeline proximity, or the January 2023 purchase stop.

## 8. Municipality election panels and official spatial sources

- **Schleswig-Holstein Landtag:** official Statistik Nord precinct returns for 7 May 2017 and 8 May 2022, the official 2022 municipality key, field dictionaries, and 2022 municipality geometry. Exact result and geometry URLs, hashes, and sizes are recorded in `data/raw/README.md`. Stable precinct IDs are aggregated to municipality; 2,485 matched 2017 districts cover 94.00% of the 2017 electorate and yield 1,097 municipal aggregates. Unmatched districts are excluded and disclosed.
- **Schleswig-Holstein local elections:** official 6 May 2018 municipality workbook and 14 May 2023 municipality results from Statistik Nord/Wahlen SH. There are 1,074 matched municipalities. Party changes are retained only where the party received votes in both elections, making turnout the most broadly comparable outcome.
- **Brandenburg Landtag:** official AfS Berlin-Brandenburg municipality aggregate workbooks for 1 September 2019 and 22 September 2024. The analysis matches 409 stable municipality keys; four changed keys are excluded.
- **BKG VG250:** municipality geometry retrieved from the official WFS `https://sgx.geodatenzentrum.de/wfs_vg250` with `typeNames=vg250_gem`, `outputFormat=application/json`, `srsName=EPSG:4326`, and bbox `11.2,51.3,14.8,53.6,EPSG:4326`; analysis filters Land code 12. BKG administrative geometry is subject to Datenlizenz Deutschland – Namensnennung – Version 2.0; retain attribution and retrieval parameters.
- **UBA PRTR:** `https://thru.de/wp-content/uploads/2026/03/prtr_2024.zip`; the official SQLite records locate PCK Raffinerie GmbH at 14.23812 E, 53.08759 N and classify it as a mineral-oil/gas refinery. The point is used for straight-line proximity only. It does not establish municipality supply, pipeline flow, or price incidence.
- **Interpretation:** these sources supply the municipality political panels requested by the user. They do not supply a local energy-price first stage. Maps, distance quartiles, and the SPUR regression are exploratory; no causal energy-price regression is claimed.

## 9. SPUR and spatially robust inference

- **Method:** Sascha O. Becker, P. David Boll, and Hans-Joachim Voth (2026), “Testing and Correcting for Spatial Unit Roots in Regression Analysis,” *Stata Journal* 26(2): 177–202, https://doi.org/10.1177/1536867X261449932; and Ulrich K. Müller and Mark W. Watson (2024), “Spatial Unit Roots and Spurious Regression,” *Econometrica* 92(5): 1661–1695, https://doi.org/10.3982/ECTA21654.
- **Software:** `spur-python` 0.1.1 and `scpc-python` 0.1.2 from the official `spatial-spur` project: https://github.com/spatial-spur/spur-python. The repository documents the full wrapper and had no open or closed issues listed at access. Installed with system/native certificate handling.
- **Specification:** Brandenburg municipality AfD second-vote change, 2019–2024, regressed on negative representative-point distance to PCK in 100 km; longitude/latitude locate observations. q=10, 20,000 simulations, seed 42, 10% decision threshold, SCPC average-correlation bound 0.03.
- **Limit:** SPUR corrects diagnostics/transformation and spatial inference. It does not validate refinery distance as an energy-price exposure or solve omitted-variable bias. The regression remains exploratory until a local price first stage exists.

## Rejected or deferred sources

- **Destatis GENESIS 61111-0011:** Monthly CPI by Land from 1995 onward, but only the all-items index; detailed energy categories are national, so it cannot supply local energy-price heterogeneity.
- **Destatis 61243:** Household gas/electricity prices are national and half-yearly, too coarse for local exposure.
- **SMARD and wholesale gas/electricity series:** National or bidding-zone outcomes; useful controls but not local retail prices.
- **Local utility tariffs and gas/electricity network charges:** Potentially relevant but no stable central historical open panel was verified; collecting operator pages would create a fragile scraping project.
- **Pipeline distance / ENTSOG or FNB maps:** Suitable for system context, not a demonstrated household retail-price exposure. Geometry, topology, and reuse conditions also complicate a reproducible local panel.
- **WSI respondent microdata:** Not publicly available as of the access date; only reports, questionnaires, and codebooks are usable.
- **Generic polling aggregators:** Non-official, heterogeneous methods, and little useful subnational resolution; GLES is preferred.
- **BKG DLM250 pipelines:** official 2022 archive route `https://daten.gdz.bkg.bund.de/produkte/dlm/dlm250/2022/dlm250.utm32s.shape.ebenen.zip` was inspected but not downloaded (about 311 MB). Geometry alone may not encode origin, flow direction, capacity, or Russian-oil dependence, so it is not a defensible treatment without further network and supply data.
