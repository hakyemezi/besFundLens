from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = Path("data")
DEFAULT_DB_PATH = DEFAULT_DATA_DIR / "besfundlens.sqlite"

URL_GENEL = "https://fonturkey.com.tr/api/funds/fonGnlBlgSiraliGetirDosya"
URL_DAGILIM = "https://fonturkey.com.tr/api/funds/dagilimSiraliGetirDosya"

DEFAULT_FON_TIPI = "EMK"
DEFAULT_LANGUAGE = "en"
