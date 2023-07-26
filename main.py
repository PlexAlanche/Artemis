import aiohttp
import asyncio
from datetime import datetime, timedelta

symbol = input("Enter a symbol to get stock data")


date_needed = datetime.now() - timedelta(days=100)
month = date_needed.strftime('%y-%m')
api_key = "LKX8H74DNJAAK2JC"

async def main():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&month={month}&outputsize=full&apikey={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.json())

asyncio.run(main())
