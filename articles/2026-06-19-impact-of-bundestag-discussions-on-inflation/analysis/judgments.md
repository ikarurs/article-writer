# Analysis Judgments

Judge: local/internal
Date: 2026-06-23
External judges: skipped; `OPENROUTER_API_KEY` not available in environment.

Scores use 1-5, where higher is better. For risk of overclaiming, 5 means low risk.

| Proposal | Feasible now | Honesty | Article value | Reproducibility | Low overclaim risk | Judgment |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Inflation Episodes Timeline | 5 | 5 | 4 | 5 | 5 | Keep |
| Before/After Inflation Surge Comparison | 5 | 4 | 4 | 5 | 4 | Keep |
| Rolling Inflation Pressure Index | 5 | 4 | 3 | 5 | 4 | Keep as supporting chart |
| Bundestag Corpus Availability Inventory | 5 | 5 | 3 | 5 | 5 | Keep as setup/limitations box |
| Inflation Mentions Over Time | 1 | 4 | 5 | 2 | 4 | Reject until debate text exists |
| Inflation vs Bundestag Attention Scatterplot | 1 | 3 | 5 | 2 | 2 | Reject until debate text exists |
| Party-Level Inflation Attention | 1 | 3 | 4 | 2 | 3 | Reject until debate text and party metadata exist |

## Objections

- The main research question needs Bundestag discussion text. Current raw files support the inflation side and the corpus acquisition plan, not discussion intensity.
- Correlations between inflation and Bundestag attention are catchy but unavailable until CPP-BT speech data or DIP text is downloaded.
- Any "impact" wording should be softened to "relationship", "attention", or "co-movement" unless a stronger design is added later.

## Recommended Selection

Use a two-part article setup for now:

1. Show the inflation episode timeline and before/after comparison from ECB HICP.
2. Add a short Bundestag data-readiness box from Zenodo CPP-BT metadata explaining what must be downloaded next to measure discussion intensity.

Do not run debate-intensity correlations yet.
