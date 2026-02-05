from mev_dex_sim.utils.types import PoolV2, Token, Trade


def test_imports_work() -> None:
    eth = Token("ETH", 18)
    usdc = Token("USDC", 6)
    pool = PoolV2(token0=eth, token1=usdc, reserve0=100.0, reserve1=200_000.0, fee_bps=30)
    trade = Trade(amount_in=50_000.0, direction="token1_to_token0")
    assert pool.reserve0 == 100.0
    assert trade.amount_in == 50_000.0
