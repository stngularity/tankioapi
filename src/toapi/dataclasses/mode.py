"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from datetime import timedelta as td
from dataclasses import dataclass
from typing import Any, Dict, List

__all__ = ("Mode",)


@dataclass
class Mode:
    """The dataclass for the game modes
    
    Attributes
    ----------
    name: :class:`str`
        The name of the mode
        
    score_earned: :class:`int`
        The count of experience points that were earned when the player
        played in this mode
        
    time_played: :class:`timedelta`
        The time in the game that was spent in this mode
        
    type: :class:`str`
        The short name of the mode"""

    name: str
    score_earned: int
    time_played: td
    type: str

    @staticmethod
    def from_list(list: List[Dict[str, Any]]) -> List["Mode"]:
        """List[:class:`Mode`]: Converts list to list with game's object
        
        Parameters
        ----------
        list: List[Dict[:class:`str`, :class:`Any`]]
            The list with dicionaries"""
        return [Mode(
            name=x["name"].strip(),
            score_earned=x["scoreEarned"],
            time_played=td(seconds=x["timePlayed"]),
            type=x["type"]
        ) for x in list]
