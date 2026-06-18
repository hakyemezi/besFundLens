# besFundLens Repository Manifest

Generated package: `besfundlens`.

## Included

- Import-safe analytics engine (`besfundlens/core/engine.py`)
- TEFAS/Fonturkey data client (`besfundlens/data/tefas_client.py`)
- Optional SQLite cache layer (`besfundlens/storage/sqlite_store.py`)
- Workflow helpers (`besfundlens/workflows.py`)
- English and Turkish sample reports
- CLI scripts for fetching, updating, generating reports, and comparing funds
- Smoke tests including a synthetic in-memory dataset

## Validation performed in sandbox

- Python compile check for all `.py` files
- Duplicate function definition check per file
- Import-safe package test without local DB
- Pytest suite: import, localization, lookback, and synthetic analytics smoke test

## Notes

The package does not include a SQLite database. Users can fetch/cache data with the provided scripts or load their own compatible DataFrames.
