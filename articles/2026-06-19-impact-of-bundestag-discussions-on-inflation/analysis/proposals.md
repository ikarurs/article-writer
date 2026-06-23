# Analysis Proposals

Proposer: current GPT model
Date: 2026-06-23

## Current Data

- ECB Germany HICP annual inflation rate, monthly, raw CSV available.
- Zenodo CPP-BT record metadata, raw JSON available.
- Bundestag/DIP plenary text is blocked pending API key.
- Destatis national CPI is blocked pending GENESIS account or browser export.
- CPP-BT speech ZIPs are deferred because the full files are large.

## Candidate Analyses

### 1. Inflation Episodes Timeline

- Data needed: ECB HICP CSV.
- Variables: `TIME_PERIOD`, `OBS_VALUE`.
- Method: plot monthly annual inflation rate and label peaks, low-inflation periods, and post-2021 surge.
- Chart/table: line chart with shaded high-inflation periods.
- Blog hook: "The inflation story MPs were reacting to was not one shock, but a sequence of waves."
- Limits/caveats: descriptive only; no Bundestag discussion data yet.
- Status: possible now.

### 2. Before/After Inflation Surge Comparison

- Data needed: ECB HICP CSV.
- Variables: monthly annual inflation rate.
- Method: compare average inflation in pre-2021, 2021-2023 surge, and post-surge periods.
- Chart/table: three-period bar chart plus table of averages and maxima.
- Blog hook: "How abnormal was the inflation period German politics had to absorb?"
- Limits/caveats: period cutoffs must be stated; no debate intensity yet.
- Status: possible now.

### 3. Rolling Inflation Pressure Index

- Data needed: ECB HICP CSV.
- Variables: monthly annual inflation rate.
- Method: compute 3-month and 12-month rolling averages.
- Chart/table: line chart comparing raw inflation with smoothed pressure.
- Blog hook: "A smoothed inflation pressure measure captures when inflation was politically hard to ignore."
- Limits/caveats: smoothing is descriptive and choice-dependent.
- Status: possible now.

### 4. Bundestag Corpus Availability Inventory

- Data needed: Zenodo CPP-BT metadata JSON.
- Variables: file names, sizes, formats, date coverage, license.
- Method: summarize which speech/protocol files are available and what each would enable.
- Chart/table: table of corpus files by format and size.
- Blog hook: "The parliamentary side of the question is measurable, but the useful files are large."
- Limits/caveats: metadata only; no discussion counts yet.
- Status: possible now.

### 5. Inflation Mentions Over Time

- Data needed: CPP-BT speeches ZIP or DIP plenary text.
- Variables: sitting date, speech text, inflation keywords.
- Method: count inflation-related mentions by month or sitting.
- Chart/table: monthly keyword-count line chart.
- Blog hook: "When inflation spiked, did Bundestag language spike too?"
- Limits/caveats: keyword counts measure attention, not sentiment or policy impact.
- Status: needs debate text.

### 6. Inflation vs Bundestag Attention Scatterplot

- Data needed: ECB HICP CSV plus monthly inflation mention counts from CPP-BT/DIP text.
- Variables: monthly inflation rate, monthly mention count or share.
- Method: scatterplot and simple correlation, optionally with 1-3 month lags.
- Chart/table: scatterplot with fitted line and lag correlation table.
- Blog hook: "Does political attention follow inflation, or anticipate it?"
- Limits/caveats: correlation only; strong risk of overclaiming causality.
- Status: needs debate text.

### 7. Party-Level Inflation Attention

- Data needed: CPP-BT speech text plus party metadata.
- Variables: party, date, speech text, inflation keyword count.
- Method: compare shares of speeches mentioning inflation by party over time.
- Chart/table: small multiples or grouped line chart.
- Blog hook: "Which parties talked about inflation most when prices rose?"
- Limits/caveats: party metadata is better from later Bundestag terms; mention counts are not policy positions.
- Status: needs debate text and party metadata.
