"""The example of working with tops"""

import asyncio
from toapi import Top, TopLists, get_tops


async def main():
    """The entrypoint of the example"""
    tops: TopLists = await get_tops()
    efficiency_top: Top = tops.efficiency
    print("----- Efficiency top -----")
    for number, user in enumerate(efficiency_top.users):
        print(f"#{number+1}   {user.name} ({user.top_value})")

if __name__ == "__main__":
    asyncio.run(main())
