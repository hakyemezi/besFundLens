from __future__ import annotations

from pathlib import Path

import pandas as pd

from besfundlens.data.tefas_client import FetchConfig, fetch_tefas_history
from besfundlens.storage.sqlite_store import load_from_sqlite


def load_from_csv(general_path: str | Path, allocation_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    return pd.read_csv(general_path), pd.read_csv(allocation_path)


def load_from_parquet(general_path: str | Path, allocation_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    return pd.read_parquet(general_path), pd.read_parquet(allocation_path)


def load_data(source: str = "sqlite", **kwargs) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load source data from sqlite, api, csv, or parquet."""
    source = source.lower()
    if source == "sqlite":
        return load_from_sqlite(kwargs["db_path"])
    if source == "api":
        return fetch_tefas_history(
            kwargs["start_date"],
            kwargs["end_date"],
            config=kwargs.get("config", FetchConfig()),
            verbose=kwargs.get("verbose", True),
        )
    if source == "csv":
        return load_from_csv(kwargs["general_path"], kwargs["allocation_path"])
    if source == "parquet":
        return load_from_parquet(kwargs["general_path"], kwargs["allocation_path"])
    raise ValueError("source must be one of: sqlite, api, csv, parquet")
