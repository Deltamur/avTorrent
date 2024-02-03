import asyncio
import aiohttp

async def check_tracker(announce_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=announce_url) as resp:
            print(resp.status)
