# War, anticipation, energy shock, and German voting

This reproducible package studies political timing below the Bundesland level. Its empirical core comprises municipality panels for the Schleswig-Holstein 2022 Landtag election, Schleswig-Holstein 2023 local election, and Brandenburg 2024 Landtag election, plus national and constituency context.

Run from this package directory:

```powershell
C:\Users\umaier\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe analysis/analysis.py
```

The run recreates processed municipality CSVs, validation/coverage tables, and PNG maps. Start with `outputs/findings.md` and `writing/outline.md`. Exact source URLs, hashes, access limits, and spatial caveats are in `sources/source-log.md` and `data/raw/README.md`.

The package does not estimate an energy-price effect. Historical local station prices and GLES microdata remain access-restricted. Refinery distance is reported as an exploratory geographic measure, including a Becker–Boll–Voth SPUR diagnostic/transformation and SCPC inference; this spatial correction does not validate distance as price exposure.
