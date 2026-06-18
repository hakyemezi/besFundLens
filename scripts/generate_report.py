from __future__ import annotations

import argparse

from besfundlens.workflows import run_universe_analysis_from_sqlite
from besfundlens.core.engine import save_markdown_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate besFundLens market narrative report from SQLite cache.")
    parser.add_argument("--db-path", default="data/besfundlens.sqlite")
    parser.add_argument("--lookback", default="1m")
    parser.add_argument("--language", choices=["en", "tr"], default="en")
    parser.add_argument("--top-n", type=int, default=10)
    parser.add_argument("--output", default="sample_reports/market_report.md")
    args = parser.parse_args()

    result = run_universe_analysis_from_sqlite(
        db_path=args.db_path,
        lookback=args.lookback,
        language=args.language,
        top_n=args.top_n,
    )
    save_markdown_report(result["markdown"], args.output)
    print(f"Report saved: {args.output}")


if __name__ == "__main__":
    main()
