from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Direction = Literal["token0_to_token1", "token1_to_token0"]


@dataclass(frozen=True, slots=True)
class Token:
    """
    Minimal token representation for simulation.
    `symbol` is for readability; `decimals` is informational for now.
    """
    symbol: str
    decimals: int = 18


@dataclass(frozen=True, slots=True)
class PoolV2:
    """
    Constant-product AMM pool representation (Uniswap v2-style).

    token0/token1 ordering is fixed for this pool instance.
    Reserves are expressed in *token units* (float for MVP simplicity).
    """
    token0: Token
    token1: Token
    reserve0: float
    reserve1: float
    fee_bps: int = 30  # 0.30% default, like Uniswap v2

    def __post_init__(self) -> None:
        if self.reserve0 < 0 or self.reserve1 < 0:
            raise ValueError("Pool reserves must be non-negative.")
        if not (0 <= self.fee_bps < 10_000):
            raise ValueError("fee_bps must be in [0, 10000).")


@dataclass(frozen=True, slots=True)
class Trade:
    """
    A single swap against a pool.
    amount_in is in units of the input token for the chosen direction.
    """
    amount_in: float
    direction: Direction

    def __post_init__(self) -> None:
        if self.amount_in <= 0:
            raise ValueError("amount_in must be > 0.")


@dataclass(frozen=True, slots=True)
class SandwichParams:
    """
    Parameters describing the MEV bot action for the sandwich.
    For MVP: only model a single front-run size (same direction as user).
    """
    front_run_amount_in: float

    def __post_init__(self) -> None:
        if self.front_run_amount_in <= 0:
            raise ValueError("front_run_amount_in must be > 0.")


@dataclass(frozen=True, slots=True)
class SimResult:
    """
    High-level simulation result for a single scenario.
    Values are in token units unless otherwise indicated.
    """
    user_amount_out: float
    user_execution_price: float  # price paid/received (quote per base) per direction convention
    user_slippage_bps: float
    mev_bot_profit_quote: float  # profit in 'quote' terms for readability (often USDC)
