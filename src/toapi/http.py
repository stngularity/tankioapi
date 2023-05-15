"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Any, Final, Mapping
from aiohttp import ClientSession, ClientResponse

try:
    import ujson as jsonlib

except ModuleNotFoundError:
    import json as jsonlib

__all__ = ("request", "request_bytes")

_BASE: Final[str] = "https://ratings.tankionline.com/api/eu"

async def request(method: str, endpoint: str) -> Mapping[str, Any]:
    """Mapping[:class:`str`, :class:`Any`]: Makes a request to API of this game
    
    Parameters
    ----------
    method: :class:`str`
        The method of the request. For example, `GET`
        
    endpoint: :class:`str`
        The endpoint of the request"""
    async with ClientSession() as session:
        response: ClientResponse = await session.request(method, _BASE+endpoint)
        return jsonlib.loads(await response.text())


async def request_bytes(method: str, endpoint: str) -> bytes:
    """:class:`bytes`: Makes a request to API of this game
    
    Parameters
    ----------
    method: :class:`str`
        The method of the request. For example, `GET`
        
    endpoint: :class:`str`
        The endpoint of the request"""
    async with ClientSession() as session:
        response: ClientResponse = await session.request(method, _BASE+endpoint)
        return await response.read()
