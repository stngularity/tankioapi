"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Any, Final, Optional, TypeVar

from aiohttp import ClientResponse, ClientSession

try:
    import ujson as jsonlib

except ModuleNotFoundError:
    import json as jsonlib

__all__ = ("request",)

_BASE: Final[str] = "https://ratings.tankionline.com/api/eu"
T = TypeVar('T')

async def request(method: str, endpoint: str, *, base: Optional[str] = None, bytes: bool = False) -> Any:
    """:class:`Any`: Makes a request to API of this game
    
    Parameters
    ----------
    method: :class:`str`
        The method of the request. For example, `GET`
        
    endpoint: :class:`str`
        The endpoint of the request
        
    base: Optional[:class:`str`]
        The base of request URL. If specified `None`, then uses
        `https://ratings.tankionline.com/api/eu`. By default, `None`
        
    bytes: :class:`bool`
        Whether to set the type of function output to :class:`bytes`. By
        default, `False`"""
    async with ClientSession() as session:
        response: ClientResponse = await session.request(method, (base or _BASE)+endpoint)

    return await response.read() if bytes else jsonlib.loads(await response.text())
