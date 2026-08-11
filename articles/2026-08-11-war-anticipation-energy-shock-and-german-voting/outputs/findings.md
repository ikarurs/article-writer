# Findings

## What changed, and when

The public evidence shows political movement both before and after Germany stopped buying Russian pipeline oil on 1 January 2023, but it does not identify a local energy-price mechanism.

In the published WSI labour-force panel, AfD support was 12% in January 2022, 16% in November 2022, and 23% in July 2023. The November point estimate was already four percentage points above the pre-invasion observation. That pattern is inconsistent with a literal chronology in which no aggregate movement occurred before January 2023. These are published weighted aggregates from a quota panel, not local or respondent-level estimates.

## Municipality evidence across the phases

The early-invasion comparison uses 2,485 common Schleswig-Holstein polling-district identifiers, representing 94.00% of the 2017 electorate and aggregated into 1,097 municipality units. Between the 2017 and 8 May 2022 Landtag elections, the median matched-sample municipal AfD second-vote change was -0.50 percentage points; the CDU median was +10.76 and the SPD median -10.81. Identical identifiers have not been proven to represent unchanged precinct boundaries, and the five-year differences include state campaigns, candidates, and the pandemic.

The first post-break contest is the Schleswig-Holstein local election of 14 May 2023. Across 1,074 matched municipalities, turnout rose by a median 1.98 points from 2018. Party changes are not broadly comparable because local lists did not run everywhere in both elections: usable samples range from 457 municipalities for the CDU to only five for the AfD. The post-break local panel therefore supports a turnout map, not a general party-gradient conclusion.

The later comparison uses official Brandenburg municipality returns for the 2019 and 22 September 2024 Landtag elections. Among 409 matched municipalities, the median AfD second-vote increase was 8.81 points. Unweighted mean changes were 10.43 points in the closest PCK-distance quartile, 7.86 and 8.73 in the middle quartiles, and 9.74 in the farthest. The table also reports valid-vote-weighted means and a centroid-distance sensitivity. The non-monotonic pattern warns against treating refinery distance alone as a linear exposure.

At the user's suggestion, the Brandenburg cross-section is also evaluated with Becker, Boll and Voth's SPUR workflow. At the 10% threshold, the AfD-change outcome fails to reject both I(0) (p=0.356) and I(1) (p=0.116); their decision rule therefore selects joint transformation of the outcome and proximity. The transformed proximity coefficient is -3.61 with an SCPC 95% interval of [-10.53, 3.31]. For transparency, the unselected levels estimate is +0.56 points per 100 km closer, with an interval of [-1.88, 2.99]. Neither branch yields a precise monotonic association, and the sign reversal reinforces the quartile warning. SPUR protects inference against persistent spatial variation; it cannot repair confounding, an invalid exposure, or missing local prices.

## Relation to Konc et al.

Konc et al. (2026) are the causal mechanism benchmark. Using four panel waves and staggered electricity-billing adjustments, they report that households receiving an above-median increase in monthly electricity instalments became 7.5 percentage points more likely to support the AfD. Their estimand is an unexpected, realised household electricity-payment shock. These municipality estimates concern election changes and refinery proximity, so the magnitudes are not directly comparable.

Kirchner's preliminary Berlin study connects predetermined local heating technology to the 2021-2023 repeat-election change. Gregor and Haucap document regional and temporal heterogeneity in fuel-price pass-through during Germany's 2022 fuel-tax cut. Both reinforce the need for a local retail-price first stage.

## Bottom line

The municipality evidence supplies the requested spatial resolution, but temporal ordering, distance quartiles, and SPUR inference cannot establish mediation through energy prices. National sentiment had moved during 2022; the matched Schleswig-Holstein sample does not show a comparable median AfD increase by May 2022; Brandenburg shows a large later increase but no precise monotonic PCK-proximity association. A causal version remains conditional on acquiring historical station prices and showing price divergence across the same municipalities.

The main files are the three municipality CSVs in `data/processed/`, `outputs/tables/spatial_coverage.csv`, `outputs/tables/brandenburg_pck_distance_gradient.csv`, and the `outputs/tables/brandenburg_spur_*` files.
