# Article outline

## Working title

**War, energy exposure, and the geography of Germany's political shift**

## Thesis

German political sentiment moved before the January 2023 end of Russian pipeline-oil purchases, while municipality election results changed unevenly across later contests. The available spatial evidence does not show a precise monotonic relationship between proximity to the PCK refinery and AfD gains. This chronology is compatible with war, expectations, inflation, and realised costs all mattering, but it does not yet identify energy prices as the mechanism.

## 1. Three elections, three points in the shock

Open with the municipality chronology rather than state totals:

- **Early invasion -- Schleswig-Holstein Landtag, 8 May 2022:** match 2,485 common polling-district identifiers from 2017 and 2022, covering 94.00% of the 2017 electorate, then aggregate them into 1,097 municipality units. The median AfD second-vote change in this matched sample was -0.50 percentage points; the CDU median was +10.76 and the SPD median -10.81.
- **First post-break election -- Schleswig-Holstein local elections, 14 May 2023:** across 1,074 matched municipalities, median turnout increased by 1.98 points from 2018. Party comparisons are sparse because local lists did not contest both elections everywhere; AfD change is comparable in only five municipalities.
- **Later adjustment -- Brandenburg Landtag, 22 September 2024:** among 409 matched municipalities, the median AfD second-vote increase from 2019 was 8.81 points.

Use the published WSI series -- 12% AfD support in January 2022, 16% in November 2022, and 23% in July 2023 -- only as a national timing marker. It shows movement during the anticipation/high-price period, not a local mechanism or within-person switching.

Suggested figure: `outputs/figures/sh_spatial_timing.png`, paired with a compact event strip marking 24 February 2022, the June 2022 embargo announcement, 1 January 2023, and the three elections.

Suggested table: `outputs/tables/spatial_coverage.csv`, expanded in the text with matched-unit and electorate coverage.

## 2. Does refinery proximity organise the later vote shift?

Explain the exploratory Brandenburg exposure measure: straight-line distance from a municipality polygon's representative point to the UBA PRTR coordinate for PCK Schwedt. It is a geographic descriptor, not a measured price shock.

Report the non-monotonic quartile pattern. Mean AfD changes were 10.43 points in the closest distance quartile, 7.86 and 8.73 in the middle quartiles, and 9.74 in the farthest quartile. Include the valid-vote-weighted estimates and centroid-distance sensitivity rather than highlighting the closest group alone.

Suggested figure: `outputs/figures/brandenburg_spatial.png`, using the maps to show heterogeneity and the scatter/decile panel to make the non-monotonic pattern visible.

Suggested table: `outputs/tables/brandenburg_pck_distance_gradient.csv`, with unweighted and weighted summaries clearly labelled.

## 3. What SPUR changes -- and what it cannot change

Motivate Becker, Boll and Voth's SPUR workflow as protection against misleading inference when spatial variables are persistent. The stationarity decision rule does not select the levels model: at the 10% threshold, the AfD-change outcome fails to reject both I(0) (p=0.356) and I(1) (p=0.116), so the analysis jointly transforms the outcome and proximity.

The selected transformed specification estimates a proximity coefficient of -3.61 with an SCPC 95% interval of [-10.53, 3.31]. The interval crosses zero. For transparency, show the unselected levels estimate of +0.56 points per 100 km closer, with an SCPC interval of [-1.88, 2.99]. Its interval also crosses zero, and the sign reversal is another warning against a simple linear proximity story.

State the boundary plainly: SPUR addresses spatial persistence and inference. It does not remove omitted-variable bias, validate refinery distance as energy exposure, or supply the missing local-price first stage.

Suggested table: `outputs/tables/brandenburg_spur_regression.csv`, accompanied by the stationarity diagnostics in `outputs/tables/brandenburg_spur_diagnostics.csv`.

## 4. A benchmark mechanism, not confirmation

Use Konc et al. as the causal household benchmark. Their four-wave panel and staggered electricity-billing adjustments imply that households receiving an above-median increase in monthly electricity instalments became 7.5 percentage points more likely to support the AfD. Their estimand is an unexpected realised household payment shock; this article's estimand is a municipality election change associated with refinery proximity. Do not compare the magnitudes mechanically.

Place Kirchner's Berlin heating-exposure study and Gregor and Haucap's evidence on regional fuel-price pass-through beside Konc et al. They motivate a local price channel, but they do not validate PCK distance as that channel in the present data.

Suggested table: the literature/design comparison, organised by unit, energy measure, political outcome, timing, and identification claim.

## 5. What the evidence can say, and the decisive next step

Conclude that the municipality results establish spatial heterogeneity and useful timing, but not mediation through energy prices. Political movement was visible nationally in 2022; the matched Schleswig-Holstein sample has a median AfD change of -0.50 points by May 2022; Brandenburg records large later gains without a precise monotonic PCK-proximity association.

Limitations that must remain visible:

- common Schleswig-Holstein precinct identifiers do not prove unchanged precinct boundaries;
- the 2023 local-election party samples are restricted by changing candidature;
- the design lacks a municipality/Kreis election outcome in the June--December 2022 anticipation phase;
- refinery distance is not a price measure and may proxy for East German geography or other confounders;
- municipality averages weight places differently from voter-weighted estimates, and small municipalities can be volatile;
- neither the chronology nor SPUR supports causal language about war, sanctions, prices, or voting.

The next-data section should be short and concrete: acquire historical Tankerkönig/MTS-K station prices, construct time-weighted daily fuel prices, aggregate them to a stable municipality vintage, and test whether prices diverged around the June 2022 announcement and 1 January 2023. Only after demonstrating pre-trends and a local price first stage should the article estimate a political gradient and rerun the stationarity/SCPC protocol using realised price exposure.

## Open questions for the author

- Should the first publication be framed as a descriptive feasibility article, or held until the municipality price panel is available?
- Is the target political outcome AfD support specifically, or a broader set of party and turnout responses?
- Should the final version add a Kreis-level outcome during the June--December 2022 anticipation phase to complete the chronology?
