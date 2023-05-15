"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass
from typing import Any, List, Mapping, Sequence, Type

from .user import TopListUser

__all__ = ("Top", "TopLists")


@dataclass
class Top:
    """The dataclass for the toplists
    
    Attributes
    ----------
    name: :class:`str`
        The name of the top
        
    users: List[:class:`TopListUser`]
        The list with users in a top"""

    name: str
    users: List[TopListUser]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name})"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    @classmethod
    def from_json(cls: Type["Top"], name: str, value: Sequence[Mapping[str, Any]]) -> "Top":
        """:class:`Top`: Converts JSON data to :class:`Top`
        
        Parameters
        ----------
        name: :class:`str`
            The name of players toplist. In the response from API, it's key
            
        value: Sequence[Mapping[:class:`str`, :class:`Any`]]
            The value of players toplist. In the response from API, it's
            value"""
        self = cls.__new__(cls)
        self.name = name
        self.users = [TopListUser.from_json(u, top=name) for u in value]
        return self


@dataclass
class TopLists:
    """The dataclass of object with the toplists
    
    Attributes
    ----------
    crystals: :class:`Top`
        The top-list of players by count of earned crystals
        
    efficiency: :class:`Top`
        The top-list of players by efficiency
    
    golds: :class:`Top`
        The top-list of players by count of caught golds
        
    score: :class:`Top`
        The top-list of players by score"""

    crystals: Top
    efficiency: Top
    golds: Top
    score: Top

    @classmethod
    def from_json(cls: Type["TopLists"], data: Mapping[str, Any]) -> "TopLists":
        """:class:`Top`: Converts JSON data to :class:`Top`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The JSON data"""
        self = cls.__new__(cls)
        self.crystals = Top("crystals", data["crystals"])
        self.efficiency = Top("efficiency", data["efficiency"])
        self.golds = Top("golds", data["golds"])
        self.score = Top("score", data["score"])
        return self
