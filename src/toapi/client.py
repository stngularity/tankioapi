"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Any, Dict, Final

from aiohttp import ClientSession, ClientResponse

from .dataclasses import Top, TopListUser, User, Rank, GameObject, Mode, Ratings, SuppliesObject
from .errors import TankiOnlineException, UserNotFoundError

try:
    import ujson as jsonlib

except ModuleNotFoundError:
    import json as jsonlib

__all__ = ("TankiOnline",)


class TankiOnline:
    """The client of Tanki Online's API.
    
    Judging by the fact that I could not find official documentation of
    this API, and it does not have a token system, the API of this game is
    not public."""

    BASE: Final[str] = "https://ratings.tankionline.com/api/eu"

    @staticmethod
    async def _request(method: str, endpoint: str) -> Dict[str, Any]:
        """Dict[:class:`str`, :class:`Any`]: Makes a request to API of this game
        
        Parameters
        ----------
        method: :class:`str`
            The method of the request. For example, `GET`
            
        endpoint: :class:`str`
            The endpoint of the request"""
        async with ClientSession() as session:
            response: ClientResponse = await session.request(method, TankiOnline.BASE+endpoint)
            return jsonlib.loads(await response.text())

    @staticmethod
    async def get_tops() -> Dict[str, Top]:
        """List[:class:`Top`]: Gets list with tops of players
        
        Raises
        ------
        :class:`TankiOnlineException`
            If it is failed to get the tops of the players"""
        response: Dict[str, Any] = await TankiOnline._request("GET", "/top")
        if response["responseType"] != "OK":
            raise TankiOnlineException("Failed to get the tops")

        output: Dict[str, Top] = {}
        for name, users in response["response"].items():
            output[name] = Top(name, [TopListUser(
                name=u["uid"],
                rank=Rank(u["rank"]),
                premium=u["hasPremium"],
                top=name,
                top_value=u["value"]
            ) for u in users])

        return output

    @staticmethod
    async def get_user(name: str, *, lang: str = "en") -> User:
        """:class:`User`: Tries to find user by the name

        Parameters
        ----------
        name: :class:`str`
            The name of the user

        lang: :class:`str`
            The language of API response. By default, `en`
        
        Raises
        ------
        :class:`UserNotFoundError`
            If user with specified :param:`name` isn't found. This error is
            possible if a player with such a name doesn't exist, or he
            disables the ability to receive information about him through
            the API"""
        response: Dict[str, Any] = await TankiOnline._request("GET", f"/profile?user={name}&lang={lang}")
        if response["responseType"] == "NOT_FOUND":
            raise UserNotFoundError(name, f"Failed to find player with \"{name}\" name")

        data: Dict[str, Any] = response["response"]
        return User(
            name=data["name"],
            rank=Rank(data["rank"]),
            premium=data["hasPremium"],
            kills=data["kills"],
            deaths=data["deaths"],
            caught_golds=data["caughtGolds"],
            drones_played=GameObject.from_list(data["dronesPlayed"]),
            crystals=data["earnedCrystals"],
            gear_score=data["gearScore"],
            hulls_played=GameObject.from_list(data["hullsPlayed"]),
            modes_played=Mode.from_list(data["modesPlayed"]),
            mounted=data["mounted"],
            paints_played=GameObject.from_list(data["paintsPlayed"]),
            presents=data["presents"],
            previous_rating=Ratings.from_json(data["previousRating"]),
            rating=Ratings.from_json(data["rating"]),
            resistance_modules=GameObject.from_list(data["resistanceModules"]),
            score=data["score"],
            score_base=data["scoreBase"],
            score_next=data["scoreNext"],
            supplies_usage=SuppliesObject.from_list(data["suppliesUsage"]),
            turrets_played=GameObject.from_list(data["turretsPlayed"])
        )
