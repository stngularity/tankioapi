"""The example of working with users information"""

import asyncio
from toapi import TankiOnline, User


async def main():
    """The entrypoint of the example"""
    user: User = await TankiOnline.get_user("sty", lang="ru")
    print(f"Name: {user.name}")
    print(f"Rank: #{user.rank.number} ({user.score}/{user.score_next} {round(user.score/user.score_next*100)}%)")
    print(f"Has premium: {'Yes' if user.premium else 'No'}")
    print()
    print(f"KD: {user.kills}/{user.deaths} ({round(user.kills/user.deaths, 2)})")
    print(f"Caught golds: {user.caught_golds}")
    print(f"Crystals: {user.crystals}")
    print(f"GS: {user.gear_score}")

if __name__ == "__main__":
    asyncio.run(main())
