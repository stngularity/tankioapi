"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass
from typing import Any, Dict, List

from .game_object import GameObject, SuppliesObject
from .mode import Mode
from .rank import Rank
from .rating import Ratings

__all__ = ("PartialUser", "TopListUser", "User")


@dataclass
class PartialUser:
    """The dataclass of partial (doesn't contain all information) user
    
    Attributes
    ----------
    name: :class:`str`
        The username (login) of the player
        
    rank: :class:`Rank`
        The current rank of the player
        
    premium: :class:`bool`
        Whether this player has a premium"""

    name: str
    rank: Rank
    premium: bool

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name=\"{self.name}\" rank={self.rank})"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name + str(self.rank.number))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, PartialUser) and other.name == self.name

    def __ne__(self, other: object) -> bool:
        return not isinstance(other, PartialUser) or other.name != self.name


@dataclass
class TopListUser(PartialUser):
    """The dataclass of user from a top
    
    Attributes
    ----------
    name: :class:`str`
        The username (login) of the player
        
    rank: :class:`Rank`
        The current rank of the player
        
    premium: :class:`bool`
        Whether this player has a premium
        
    top: :class:`str`
        The name of the top which this player from
        
    top_value: :class:`int`
        The value of the characteristic of this player, according to which
        the :attr:`top` was compiled"""

    top: str
    top_value: int


@dataclass
class User(PartialUser):
    """The dataclass of user from a top
    
    Attributes
    ----------
    name: :class:`str`
        The username (login) of the player
        
    rank: :class:`Rank`
        The current rank of the player
        
    premium: :class:`bool`
        Whether this player has a premium
        
    kills: :class:`int`
        The count of player's kills
        
    deaths: :class:`int`
        The count of player's deaths
        
    caught_golds: :class:`int`
        The count of golds which caught by this player
        
    drones_played: List[:class:`GameObject`]
        The list with drones which the player is played on
        
    crystals: :class:`int`
        The count of crystals which this player earned
        
    gear_score: :class:`int`
        The gear score of this player
        
    hulls_played: List[:class:`GameObject`]
        The list of hulls which the player is played on
        
    modes_played: List[:class:`Mode`]
        The list of modes which the player is played at
        
    mounted: Dict[:class:`str`, :class:`str`]
        Dictionary where key is a single value from `armor`, `paint` and
        `weapon`, and value is an image URL with `.tnk` extension (renamed
        `.png`)
        
    paints_played: List[:class:`GameObject`]
        The list of paints which the player is played on
        
    presents: List[:class:`Any`]
        Sorry, I don't know what is storage by this key
        
    previous_rating: :class:`Ratings`
        The rating which the player had early
        
    rating: :class:`Ratings`
        The rating which the player has currently
        
    resistance_modules: List[:class:`GameObject`]
        The list of resistance modules which the player is played on
        
    score: :class:`int`
        This player's current score points
        
    score_base: :class:`int`
        The score points that were needed in order to get the current
        player rank
        
    score_next: :class:`int`
        Score points that are needed in order to get the next rank
        
    supplies_usage: List[:class:`SuppliesObject`]
        A list with supplies and the amount of their use by this player
        
    turrets_played: List[:class:`GameObject`]
        The list of turrets which the player is played on"""

    kills: int
    deaths: int
    caught_golds: int
    drones_played: List[GameObject]
    crystals: int
    gear_score: int
    hulls_played: List[GameObject]
    modes_played: List[Mode]
    mounted: Dict[str, str]
    paints_played: List[GameObject]
    presents: List[Any]
    previous_rating: Ratings
    rating: Ratings
    resistance_modules: List[GameObject]
    score: int
    score_base: int
    score_next: int
    supplies_usage: List[SuppliesObject]
    turrets_played: List[GameObject]
