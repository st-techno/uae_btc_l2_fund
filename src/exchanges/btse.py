import aiohttp
from typing import Optional, Dict

class BTSEClient:
    def __init__(self, api_key: str, secret: str):
        self.api_key = api_key
        self.secret = secret
        self.base_url = "https://api.btse.com/api/v1"
    
    async def get_satbtc_price(self, session: aiohttp.ClientSession) -> Optional[Dict]:
        """Fetch satBTC-USDT price from BTSE UAE"""
        async with session.get(f"{self.base_url}/market/satBTC_USDT") as resp:
            return await resp.json()
