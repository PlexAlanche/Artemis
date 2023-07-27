
import aiohttp
import asyncio
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

symbol = "ibm"


date_needed = datetime.now() - timedelta(days=100)
month = date_needed.strftime('%y-%m')
api_key = "LKX8H74DNJAAK2JC"

async def main():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&month={month}&outputsize=full&apikey={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.json())
        Path('stock.json').write_text(str(resp.json()).replace("'", '"').replace('Meta Data', 'ds').replace('Time Series (Daily)', 'y'))

df = pd.read_json('stock.json')

asyncio.run(main())
