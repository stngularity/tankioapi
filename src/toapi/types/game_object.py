"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

# pylint: disable=C0103

from dataclasses import dataclass
from datetime import timedelta as td
from typing import Any, List, Mapping, Optional, Type

from ..http import request

__all__ = ("GameObject", "SuppliesObject")


@dataclass
class BaseGameObject:
    """The base dataclass for the objects from Tanki Online
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the game's object
        
    image: :class:`str`
        The URL to the image of this object. The image is `.tnk` file, but
        it's possible to render as `.png`
        
    name: :class:`str`
        The name of the object"""

    id: int
    image: str
    name: str

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name=\"{self.name}\")"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.id)

    async def read_image(self) -> bytes:
        """:class:`bytes`: Reads the image data of this object and returns it"""
        return await request("GET", self.image, base="", bytes=True)


@dataclass
class GameObject(BaseGameObject):
    """The dataclass for the objects from Tanki Online
    
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
    properties: Optional[List[str]]
    score_earned: int
    time_played: td

    @classmethod
    def from_json(cls: Type["GameObject"], data: Mapping[str, Any]) -> "GameObject":
        """:class:`GameObject`: Converts JSON data to :class:`GameObject`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The JSON data"""
        self = cls.__new__(cls)
        self.grade = data["grade"] + 1
        self.id = data["id"]
        self.image = data["imageUrl"]
        self.name = data["name"]
        self.properties = data["properties"]
        self.score_earned = data["scoreEarned"]
        self.time_played = td(seconds=data["timePlayed"])
        return self

    @staticmethod
    def from_list(list: List[Mapping[str, Any]]) -> List["GameObject"]:
        """List[:class:`GameObject`]: Converts list to list with game's object
        
        Parameters
        ----------
        list: List[Mapping[:class:`str`, :class:`Any`]]
            The list with Mappingionaries"""
        return [GameObject.from_json(x) for x in list]


@dataclass
class SuppliesObject(BaseGameObject):
    """The dataclass for the supplies objects from Tanki Online
    
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

    usages: int

    @classmethod
    def from_json(cls: Type["SuppliesObject"], data: Mapping[str, Any]) -> "SuppliesObject":
        """:class:`SuppliesObject`: Converts JSON data to :class:`SuppliesObject`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The JSON data"""
        self = cls.__new__(cls)
        self.id = data["id"]
        self.image = data["imageUrl"]
        self.name = data["name"]
        self.usages = data["usages"]
        return self

    @staticmethod
    def from_list(list: List[Mapping[str, Any]]) -> List["SuppliesObject"]:
        """List[:class:`SuppliesObject`]: Converts list to list with supplies
        
        Parameters
        ----------
        list: List[Mapping[:class:`str`, :class:`Any`]]
            The list with dicionaries"""
        return [SuppliesObject.from_json(x) for x in list]
