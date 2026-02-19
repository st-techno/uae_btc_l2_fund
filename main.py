#!/usr/bin/env python3
"""
UAE BTC L2 Arbitrage Fund - Production Entry Point
VARA/ADGM Licensed Entity
"""
import asyncio
import logging
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from arbitrage.vault_arb import UAEArbitrageFund
from utils.logger import setup_logger

async def main():
    logger = setup_logger()
    logger.info("🚀 Starting UAE BTC L2 Arbitrage Fund")
    
    fund = UAEArbitrageFund()
    await fund.run()

if __name__ == "__main__":
    asyncio.run(main())
