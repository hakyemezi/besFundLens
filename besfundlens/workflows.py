from __future__ import annotations

from typing import Optional, Sequence, Union

from besfundlens.core.engine import (
    DEFAULT_LANGUAGE,
    initialize_engine,
    run_universe_analysis,
    compare_funds,
    selected_funds_report_to_markdown,
)
from besfundlens.data.loaders import load_data
from besfundlens.storage.sqlite_store import update_sqlite_cache


def run_universe_analysis_from_sqlite(
    db_path,
    lookback: Optional[Union[str, int]] = "1m",
    valid_only: bool = True,
    language: str = DEFAULT_LANGUAGE,
    top_n: int = 10,
) -> dict:
    df_general, df_allocation = load_data(source="sqlite", db_path=db_path)
    initialize_engine(df_general, df_allocation)
    return run_universe_analysis(
        lookback=lookback,
        valid_only=valid_only,
        language=language,
        top_n=top_n,
    )


def compare_funds_from_sqlite(
    db_path,
    fund_codes: Sequence[str],
    lookback: Optional[Union[str, int]] = "1m",
    sort_by: Optional[str] = None,
    ascending: bool = False,
):
    df_general, df_allocation = load_data(source="sqlite", db_path=db_path)
    initialize_engine(df_general, df_allocation)
    return compare_funds(
        fund_codes=fund_codes,
        lookback=lookback,
        sort_by=sort_by,
        ascending=ascending,
    )


def build_or_update_cache_then_run(
    db_path,
    start_date=None,
    end_date=None,
    lookback: Optional[Union[str, int]] = "1m",
    language: str = DEFAULT_LANGUAGE,
    top_n: int = 10,
    verbose: bool = True,
) -> dict:
    update_info = update_sqlite_cache(
        db_path=db_path,
        start_date=start_date,
        end_date=end_date,
        verbose=verbose,
    )
    result = run_universe_analysis_from_sqlite(
        db_path=db_path,
        lookback=lookback,
        language=language,
        top_n=top_n,
    )
    result["update_info"] = update_info
    return result


def selected_funds_markdown_from_sqlite(
    db_path,
    fund_codes: Sequence[str],
    lookback: Optional[Union[str, int]] = "1m",
    language: str = DEFAULT_LANGUAGE,
) -> str:
    comparison_df = compare_funds_from_sqlite(
        db_path=db_path,
        fund_codes=fund_codes,
        lookback=lookback,
    )
    return selected_funds_report_to_markdown(comparison_df, language=language)
