from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class VaultMetrics:
    symbol: str
    btc_equivalent: Decimal
    premium_bp: Decimal
    tvl_usd: float
    apr_pct: float
    liquidity_usd: float
    timestamp: float
    chain: str
