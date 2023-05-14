"""The example of working with tops"""

import asyncio
from typing import Dict

from toapi import TankiOnline, Top


async def main():
    """The entrypoint of the example"""
    tops: Dict[str, Top] = await TankiOnline.get_tops()
    for top in tops.values():
        print(f"----- {top.name} -----")
        for number, user in enumerate(top.users):
            print(f"#{number+1}   {user.name} ({user.top_value})")

        print()

if __name__ == "__main__":
    asyncio.run(main())
