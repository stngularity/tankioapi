"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from datetime import timedelta as td
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

__all__ = ("GameObject", "SuppliesObject")


@dataclass
class GameObject:
    """The dataclass of the object from Tanki Online
    
    Attributes
    ----------
    grade: :class:`int`
        The level of the object (Mk-`N`, where `N` is the level). If the
        object doesn't have such a property (that's, our object is a drone
        or paint), then it's equal to `-1`
        
    id: :class:`int`
        The ID of the game's object
        
    image: :class:`str`
        The URL to the image of this object. The image is `.tnk` file, but
        it's possible to render as `.png`
        
    name: :class:`str`
        The name of the object
        
    properties: Optional[List[:class:`str`]]
        The list with properties of this object. In most cases it's `None`
        
    score_earned: :class:`int`
        The count of experience points that were earned when the player
        played with this object
        
    time_played: :class:`timedelta`
        The time in the game that was spent with these objects"""

    grade: int
    id: int
    image: str
    name: str
    properties: Optional[List[str]]
    score_earned: int
    time_played: td

    @staticmethod
    def from_list(list: List[Dict[str, Any]]) -> List["GameObject"]:
        """List[:class:`GameObject`]: Converts list to list with game's object
        
        Parameters
        ----------
        list: List[Dict[:class:`str`, :class:`Any`]]
            The list with dicionaries"""
        return [GameObject(
            grade=x["grade"]+1,
            id=x["id"],
            image=x["imageUrl"],
            name=x["name"],
            properties=x["properties"],
            score_earned=x["scoreEarned"],
            time_played=td(seconds=x["timePlayed"])
        ) for x in list]


@dataclass
class SuppliesObject:
    """The dataclass of the supplies object from Tanki Online
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the game's object
        
    image: :class:`str`
        The URL to the image of this object. The image is `.tnk` file, but
        it's possible to render as `.png`
        
    name: :class:`str`
        The name of the object
        
    usages: :class:`int`
        The count of these supplies usages"""

    id: int
    image: str
    name: str
    usages: int

    @staticmethod
    def from_list(list: List[Dict[str, Any]]) -> List["SuppliesObject"]:
        """List[:class:`SuppliesObject`]: Converts list to list with supplies
        
        Parameters
        ----------
        list: List[Dict[:class:`str`, :class:`Any`]]
            The list with dicionaries"""
        return [SuppliesObject(
            id=x["id"],
            image=x["imageUrl"],
            name=x["name"],
            usages=x["usages"]
        ) for x in list]
