from pathlib import Path
from pydantic import BaseSettings
from typing import Dict

class UAEConfig(BaseSettings):
    min_profit_bp: float = 15
    max_position_usd: int = 500_000
    poll_interval: float = 3.0
    
    class Config:
        env_file = ".env"

config = UAEConfig()
