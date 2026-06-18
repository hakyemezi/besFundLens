from __future__ import annotations

from besfundlens.workflows import compare_funds_from_sqlite
from besfundlens.core.engine import selected_funds_report_to_markdown

DB_PATH = "data/besfundlens.sqlite"
FUNDS = ["AAJ", "MHD", "MEA"]

comparison = compare_funds_from_sqlite(
    db_path=DB_PATH,
    fund_codes=FUNDS,
    lookback="1m",
    sort_by="market_effect_pct",
    ascending=False,
)

print(selected_funds_report_to_markdown(comparison, language="en"))
print()
print(selected_funds_report_to_markdown(comparison, language="tr"))
