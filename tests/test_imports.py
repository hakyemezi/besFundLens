from besfundlens import BUILD_VERSION, resolve_lookback_intervals
from besfundlens.core.engine import translate_quadrant_name


def test_version_available():
    assert "repo-stable" in BUILD_VERSION


def test_lookback_presets():
    assert resolve_lookback_intervals("1m") == 20
    assert resolve_lookback_intervals("3m") == 60
    assert resolve_lookback_intervals(45) == 45


def test_tr_quadrant_translation():
    assert translate_quadrant_name("Negative Market / Negative Flow", "tr") == "Negatif Piyasa / Negatif Akış"
