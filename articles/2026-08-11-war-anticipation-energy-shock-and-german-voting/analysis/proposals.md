# Analysis Proposals

These candidates are descriptive unless stated otherwise. The public election files can document when and where voting changed, but they cannot by themselves identify an energy-price mechanism.

## 1. Berlin's same-office before/after snapshot

- **Status:** Feasible now.
- **Data needed:** `data/raw/elections/state/berlin_agh_2021_2023.xlsx`.
- **Variables:** Polling district or smallest common geography; eligible voters; turnout; valid votes; party list-vote counts and shares in the 2021 election and February 2023 repeat election.
- **Method:** Harmonise the two election sheets to common geographic identifiers; calculate percentage-point changes in turnout and party shares; report median, interquartile range, and the distribution across districts.
- **Chart/table:** Small-multiple maps or ranked dot plots of district-level changes for AfD, Greens, SPD, CDU, and Die Linke; compact turnout-change table.
- **Likely blog hook:** “Berlin voted on the same office before and after the energy shock—what changed neighbourhood by neighbourhood?”
- **Limits/caveats:** The repeat election was triggered by failures in the 2021 election, so turnout and administrative corrections are major confounders. Other political events occurred between elections. This is not an energy-price or causal estimate; exclude or flag unmatched and special/brief-vote districts.

## 2. Lower Saxony constituencies from 2017 to October 2022

- **Status:** Feasible now.
- **Data needed:** `data/raw/elections/state/ni_landtag_2017.csv` and `ni_landtag_2022.csv`.
- **Variables:** `Wahlkreis`; eligible voters; voters; valid second votes; party second-vote counts (`… II`) for CDU, SPD, Greens, FDP, AfD, and Die Linke.
- **Method:** Match common constituency identifiers, convert counts to shares, and calculate 2017–2022 percentage-point changes and turnout changes. Show both unweighted constituency distributions and electorate-weighted statewide summaries.
- **Chart/table:** Slope chart of statewide party shares plus a constituency scatter or ranked bar chart of AfD/Green changes.
- **Likely blog hook:** “By the first autumn of the energy crisis, Lower Saxony's electoral map had shifted—but not uniformly.”
- **Limits/caveats:** Only roughly 87 constituencies; boundary or numbering changes must be checked. The five-year interval includes the pandemic, government turnover, candidate effects, and many other shocks. There is no local energy-price variable in the current package.

## 3. Nationwide polling-district change, Bundestag 2021 to 2025

- **Status:** Feasible now after raw extraction and geographic validation.
- **Data needed:** `data/raw/elections/btw21_wbz.zip` and `btw25_wbz.zip`, including result and municipality-guide CSVs.
- **Variables:** Municipality key; polling-district type; eligible voters; turnout; valid second votes; party second-vote counts/shares.
- **Method:** Aggregate each election to harmonised municipalities rather than force unstable polling-district matches; calculate party-share and turnout changes; summarise distributions by Land and East/West.
- **Chart/table:** Germany map of municipal AfD change with companion box plots by Land; table of electorate-weighted party changes.
- **Likely blog hook:** “The national shift was not one shift: 2021–2025 changes looked very different across German municipalities.”
- **Limits/caveats:** The 2025 election is three years after the invasion and followed a changed party system, including BSW. Municipality mergers, Berlin's repeat-election history, brief-vote allocation, and party comparability require explicit rules. Without exposure data, regional patterns must not be attributed to energy prices.

## 4. The 2024 European election as a midpoint

- **Status:** Feasible now, best used as a secondary descriptive bridge.
- **Data needed:** All three official ZIPs: Bundestag 2021, European election 2024, and Bundestag 2025.
- **Variables:** Harmonised municipality; turnout; valid votes; comparable party vote shares at each election.
- **Method:** Build a three-date municipality panel and show whether places with large 2021–2025 changes had already moved in the same direction by June 2024. Use within-election shares and standardised municipality ranks rather than treating levels across election types as directly equivalent.
- **Chart/table:** Three-column rank or change-quadrant chart for major parties; map categories such as “shift visible by 2024” versus “shift mainly after 2024.”
- **Likely blog hook:** “Was Germany's 2025 realignment already visible in the 2024 European vote?”
- **Limits/caveats:** European and federal elections have different turnout, stakes, candidates, and strategic voting. BSW did not exist in 2021. This is timing context, not a sanctions test or a clean outcome panel.

## 5. Published WSI panel timeline: burdens and vote intention

- **Status:** Feasible now as a transparent reproduction of published aggregates, not a new microdata analysis.
- **Data needed:** `data/raw/context/p_wsi_report_92_2023.pdf` (or the English duplicate for checking).
- **Variables:** Published Sunday-question or actual second-vote shares for July 2021, October 2021, January 2022, November 2022, and July 2023; published perceived price/energy burdens, financial worries, AfD switching groups, and East/West splits where reported.
- **Method:** Transcribe only explicitly reported values with page/table references; plot the published timeline and place invasion and energy-crisis milestones only after their official dates are logged.
- **Chart/table:** Annotated party-intention timeline paired with one burden indicator; source-note table of sample sizes and question wording by wave.
- **Likely blog hook:** “The same workers were asked before and during the crisis: perceived pressure rose alongside a changing party landscape.”
- **Limits/caveats:** WSI microdata are unavailable, so no recomputation, uncertainty estimates, custom subgroups, or individual-level linkage is possible. The Payback quota panel covers labour-force participants, not all voters. Co-movement in published aggregates is not evidence that burdens changed votes.

## 6. GLES event-time sentiment sequence

- **Status:** Needs credentialed GLES download.
- **Data needed:** Tracking T51–T59; optionally Panel Waves 22–28; dataset-specific questionnaires, weights, and licenses.
- **Variables:** Wave/interview date; Sunday-question vote intention; government and party evaluations; economic expectations; issue salience; Ukraine, war, or energy questions where wording repeats; Bundesland/East-West; weights and stable panel respondent ID where available.
- **Method:** Weighted wave means with confidence intervals, anchored on T51 as the closest pre-invasion cross-section. Use the panel only for within-person transition tables between adjacent comparable waves. Separate invasion, gas-supply, and sanctions markers rather than label all post-February observations as one treatment.
- **Chart/table:** Event-time line chart by party or East/West; Sankey or transition matrix for panel vote intention if stable IDs and identical questions are documented.
- **Likely blog hook:** “Germany's last pre-invasion survey was ten days before the attack—what moved in the next waves?”
- **Limits/caveats:** Registration is currently blocking access. Modules, wording, samples, and weights vary; T52 is already months after the invasion. National energy prices and political sentiment share time trends, so before/after movement remains associational.

## 7. Local fuel-price shock and later voting

- **Status:** Needs authenticated Tankerkönig history; optional official national benchmark prices should also be added.
- **Data needed:** MTS-K/Tankerkönig station metadata and daily price changes for 2021–2024, plus official election ZIPs.
- **Variables:** Station UUID, timestamp, valid E5/E10/diesel EUR/litre, coordinates/postcode, station status; harmonised municipality; later turnout and party vote shares.
- **Method:** Reconstruct time-weighted daily station prices, aggregate robustly to municipality-week, and describe pre/post changes around separately documented invasion and sanctions dates. Compare the distribution of local price changes, then use binned scatterplots against subsequent municipal vote-share changes with pre-period political levels shown separately.
- **Chart/table:** Map of municipal peak fuel-price change; weekly quantile fan chart; binned scatter of price shock versus later AfD/Green/turnout change.
- **Likely blog hook:** “Germany shared a national oil shock, but local pump prices did not move in lockstep—did later political shifts line up with that variation?”
- **Limits/caveats:** Archive access and reuse terms are currently blocking acquisition. Fuel is not household gas or electricity; pipeline/refinery distance does not prove supply exposure. Local competition, taxes, commuting, urbanity, and baseline politics can drive both prices and voting. Present correlations only, and do not claim an energy channel from proximity alone.
