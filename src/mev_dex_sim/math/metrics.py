from __future__ import annotations

from .constants import BPS_DENOMINATOR, EPS


def to_bps(ratio: float) -> float:
    """
    Convert a ratio (e.g., 0.0123 for 1.23%) to basis points.
    """
    return ratio * BPS_DENOMINATOR


def bps_change(actual: float, expected: float) -> float:
    """
    Return (actual - expected) / expected in basis points.
    Positive means actual > expected.
    """
    if abs(expected) < EPS:
        raise ValueError("expected must be non-zero for bps_change.")
    return to_bps((actual - expected) / expected)


def pct_change(actual: float, expected: float) -> float:
    """
    Return (actual - expected) / expected as a percentage (e.g., 1.23 = 1.23%).
    """
    if abs(expected) < EPS:
        raise ValueError("expected must be non-zero for pct_change.")
    return 100.0 * (actual - expected) / expected


def format_usd(x: float) -> str:
    """
    Simple USD formatting helper for reports.
    """
    sign = "-" if x < 0 else ""
    x = abs(x)
    return f"{sign}${x:,.2f}"
