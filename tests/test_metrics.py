import pytest

from mev_dex_sim.math.metrics import bps_change, format_usd, to_bps


def test_to_bps() -> None:
    assert to_bps(0.01) == 100.0


def test_bps_change() -> None:
    # actual 105 vs expected 100 => +5% => +500 bps
    assert bps_change(105.0, 100.0) == 500.0


def test_bps_change_raises_on_zero_expected() -> None:
    with pytest.raises(ValueError):
        bps_change(1.0, 0.0)


def test_format_usd() -> None:
    assert format_usd(1234.5) == "$1,234.50"
    assert format_usd(-12.3) == "-$12.30"
