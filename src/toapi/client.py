"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Any, Mapping

from .types import TopLists, User
from .errors import TankiOnlineException, UserNotFoundError
from .http import request

__all__ = ("get_tops", "get_user")


async def get_tops() -> TopLists:
    """List[:class:`Top`]: Gets list with tops of players
    
    Raises
    ------
    :class:`TankiOnlineException`
        If it is failed to get the tops of the players"""
    response: Mapping[str, Any] = await request("GET", "/top")
    if response["responseType"] != "OK":
        raise TankiOnlineException("Failed to get the tops")

    return TopLists.from_json(response["response"])


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
    response: Mapping[str, Any] = await request("GET", f"/profile?user={name}&lang={lang}")
    if response["responseType"] == "NOT_FOUND":
        raise UserNotFoundError(name, f"Failed to find player with \"{name}\" name")

    return User.from_json(response["response"])
