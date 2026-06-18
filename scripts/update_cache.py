from __future__ import annotations

import argparse

from besfundlens.storage.sqlite_store import update_sqlite_cache


def main() -> None:
    parser = argparse.ArgumentParser(description="Incrementally update a SQLite BES fund cache.")
    parser.add_argument("--db-path", default="data/besfundlens.sqlite", help="SQLite database path")
    parser.add_argument("--start", default=None, help="Optional explicit start date")
    parser.add_argument("--end", default=None, help="Optional explicit end date")
    parser.add_argument("--overlap-days", type=int, default=2)
    args = parser.parse_args()

    info = update_sqlite_cache(
        db_path=args.db_path,
        start_date=args.start,
        end_date=args.end,
        overlap_days=args.overlap_days,
        verbose=True,
    )
    print(info)


if __name__ == "__main__":
    main()
