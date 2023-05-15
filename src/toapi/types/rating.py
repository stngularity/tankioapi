"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass
from typing import Any, Dict, Optional, Type

__all__ = ("Rating", "Ratings")


@dataclass
class Rating:
    """The dataclass for the rating
    
    Attributes
    ----------
    position: :class:`int`
        The position of the player in any top
        
    value: :class:`int`
        The value of characteristic of the player, according to which the
        top was compiled"""

    position: int
    value: int

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(position={self.position}, value={self.value})"

    def __str__(self) -> str:
        return f"#{self.position}"

    def __hash__(self) -> int:
        return hash(self.value)


@dataclass
class Ratings:
    """The dataclass for the player's ratings
    
    Attributes
    ----------
    crystals: Optional[:class:`Rating`]
        The rating by the count of crystals
        
    efficiency: Optional[:class:`Rating`]
        The rating by the player's efficiency
        
    golds: Optional[:class:`Rating`]
        The rating by the count of caught golds
        
    score: Optional[:class:`Rating`]
        The rating by the score"""

    crystals: Optional[Rating]
    efficiency: Optional[Rating]
    golds: Optional[Rating]
    score: Optional[Rating]

    @classmethod
    def from_json(cls: Type["Ratings"], data: Dict[str, Any]) -> "Ratings":
        """:class:`Ratings`: Converts JSON to :class:`Ratings`
        
        Parameters
        ----------
        data: Dict[:class:`str`, :class:`Any`]
            The original data of ratings"""
        self = cls.__new__(cls)
        self.crystals = Rating(**data["crystals"]) if data["crystals"] is not None else None
        self.efficiency = Rating(**data["efficiency"]) if data["efficiency"] is not None else None
        self.golds = Rating(**data["golds"]) if data["golds"] is not None else None
        self.score = Rating(**data["score"]) if data["score"] is not None else None
        return self
