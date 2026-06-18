from __future__ import annotations

import argparse

from besfundlens.data.tefas_client import FetchConfig, fetch_tefas_history
from besfundlens.storage.sqlite_store import save_full_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch historical BES fund data and save it to SQLite.")
    parser.add_argument("--start", required=True, help="Start date, e.g. 2021-06-15")
    parser.add_argument("--end", required=True, help="End date, e.g. 2026-06-15")
    parser.add_argument("--db-path", default="data/besfundlens.sqlite", help="SQLite database path")
    parser.add_argument("--timeout", type=int, default=40)
    parser.add_argument("--max-retries", type=int, default=5)
    args = parser.parse_args()

    config = FetchConfig(timeout=args.timeout, max_retries=args.max_retries)
    df_general, df_allocation = fetch_tefas_history(args.start, args.end, config=config, verbose=True)
    save_full_snapshot(args.db_path, df_general, df_allocation, if_exists="replace")
    print(f"Saved general rows: {len(df_general):,}")
    print(f"Saved allocation rows: {len(df_allocation):,}")
    print(f"Database path: {args.db_path}")


if __name__ == "__main__":
    main()
