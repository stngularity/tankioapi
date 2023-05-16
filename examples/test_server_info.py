"""The example of working with information about test servers"""

import asyncio
from typing import List

from toapi import TestServerStatus, get_test_status


async def main():
    """The entrypoint of the example"""
    servers: List[TestServerStatus] = await get_test_status()
    print(f"Total {len(servers)} test servers\n")
    for server in servers:
        print(f"{server.release}: {server.domain}; {server.user_count} users and {len(server.nodes)} nodes")

if __name__ == "__main__":
    asyncio.run(main())
