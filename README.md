## Bitcoin L2 Arbitrage Fund Bot - UAE Registered Entity (VARA/ADGM Compliant)

Arbitrage across satBTC (Core Chain), sBTC (Stacks), mrBTC (Babylon restaking)

Real-time premium/discount trading + cross-L2 basis trades vs wstETH benchmark

UAE Compliance: VASP licensed, 0% corp tax (DIFC), 9% VAT on services only

WARNING: Production deployment requires ADGM VARA API keys + MEV protection

# Deployment Commands - BASH

# 1. Build & test

docker build -t uae-l2-fund .

docker run --rm uae-l2-fund python -m pytest tests/

# 2. Production deploy (Dubai AWS)

docker run -d \

  --name uae-l2-fund \
  
  --restart always \
  
  -v $(pwd)/logs:/app/logs \
  
  -v $(pwd)/config:/app/config \
  uae-l2-fund

# 3. Monitor

docker logs -f uae-l2-fund

tail -f logs/uae_fund.log

# EXECUTION - BASH

cd uae_btc_l2_fund

python main.py    # Development

docker run ...    # Production


