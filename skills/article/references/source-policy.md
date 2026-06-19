# Source Policy

Prefer official and trusted API sources before exploratory material:

- national statistical offices, central banks, ministries, regulators, and international institutions;
- documented public APIs with stable retrieval URLs;
- peer-reviewed, institutional, or otherwise auditable datasets.

Exploratory or user-provided sources are allowed only when useful context cannot be captured from trusted APIs alone. Log them in `sources/source-log.md` with the access date, URL or file path, why they were used, and any reliability caveat.

Preserve raw downloaded data in `data/raw/` unless license or API terms forbid it. If raw data cannot be stored, record retrieval instructions, endpoint, parameters, date accessed, and the reason the raw file is omitted.
