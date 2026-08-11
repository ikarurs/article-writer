# Analysis Judgments

Judge: local/internal (no `OPENROUTER_API_KEY` available)  
Date: 2026-08-11

Scores run from 1 (weak) to 5 (strong). For overclaim risk, 5 means low risk.

| # | Proposal | Feasible now | Statistical honesty | Article value | Reproducibility | Low overclaim risk | Decision |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | Berlin 2021/2023 snapshot | 5 | 4 | 4 | 4 | 4 | Include narrowly |
| 2 | Lower Saxony 2017/2022 | 5 | 4 | 4 | 4 | 4 | Include narrowly |
| 3 | Bundestag 2021/2025 municipalities | 4 | 4 | 4 | 4 | 4 | Defer |
| 4 | 2024 European-election midpoint | 4 | 4 | 4 | 4 | 3 | Defer |
| 5 | Published WSI panel timeline | 5 | 5 | 5 | 4 | 4 | Core analysis |
| 6 | GLES event-time sequence | 1 | 4 | 5 | 1 | 3 | Reject for v1 |
| 7 | Local fuel-price shock and voting | 1 | 3 | 5 | 1 | 2 | Reject for v1 |

## Judgment

The minimum honest v1 combines proposal 5 with the small, complementary pieces of proposals 2 and 1. The WSI report supplies pre-war, anticipation, and post-January-2023 sentiment observations. Lower Saxony supplies an actual election during the anticipation/high-price phase, and Berlin supplies an actual same-office comparison immediately after the pipeline-purchase stop. These sources describe timing; they do not identify an energy-price channel.

Do not build the nationwide municipality panel yet. It adds substantial boundary harmonisation while still lacking local energy exposure. Preserve the downloaded federal/European files and retrieval notes for the later full design.

## Objections and required caveats

- WSI values are published aggregates from a labour-force quota panel, not available respondent microdata. Do not compute new uncertainty, transitions, or subgroup estimates, and do not present aggregate co-movement as individual switching.
- Lower Saxony compares 2017 with 2022. Pandemic effects, candidates, government performance, and the full five-year political cycle are inseparable from war or energy expectations.
- Berlin's 2023 election was a repeat caused by administrative failures in 2021. Turnout corrections and other events are major confounders; it is a benchmark, not a natural experiment.
- The two elections have different offices, geographies, and electorates. Never stack or directly compare their raw levels, and never call their differences a treatment effect.
- Event labels describe calendar timing only. January 2023 marks Germany's end of Russian pipeline-oil purchases, not the start of the broader energy-price shock.
- State-file provenance and exact official URLs must be added to the source log before the package is declared reproducible.

## Rejected for v1

- **Proposal 6:** GLES registration blocks the required microdata and documentation. Retrieval notes remain the upgrade path.
- **Proposal 7:** authenticated Tankerkoenig history is unavailable, so there is no local price first stage or defensible price-exposure measure. No energy-price regression, refinery-distance proxy, or causal mediation claim is permitted.

## Revision after the municipality/Kreis requirement

The user subsequently required geography below Bundesland level. That instruction supersedes the earlier recommendation to stop with contextual state evidence. The revised feasible choice is a three-panel municipality chronology: stable Schleswig-Holstein Landtag precincts aggregated to municipality (2017–2022), Schleswig-Holstein municipality local-election returns (2018–2023), and Brandenburg municipality Landtag returns (2019–2024). Refinery distance is admitted only as a mapped descriptive covariate; the rejection of an energy-price regression remains in force because no local price first stage is available. Lower Saxony and Berlin are retained as context, not core results.
