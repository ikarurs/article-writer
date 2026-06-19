# Package Contract

Every article package must contain:

- `article.yaml`
- `README.md`
- `sources/source-log.md`
- `sources/citations.bib`
- `data/raw/`
- `data/processed/`
- `analysis/analysis.py`
- `outputs/figures/`
- `outputs/tables/`
- `outputs/findings.md`
- `writing/outline.md`
- `writing/notes.md`

`article.yaml` records topic, date, package path, sources, commands run, agent notes, and reproducibility status. Keep it plain YAML that can be read without project-specific tooling.
