# Data Source and Cache Notes

The original research scripts used Fonturkey/TEFAS-style public endpoints for Turkish pension fund general information and allocation data.

The public repo version separates this into:

- `besfundlens.data.tefas_client`: API fetching
- `besfundlens.storage.sqlite_store`: optional SQLite cache
- `besfundlens.core.engine`: analytics engine working from DataFrames

SQLite is recommended for repeated analysis, but it is not mandatory.
