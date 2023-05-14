"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass

__all__ = ("Rank",)


@dataclass
class Rank:
    """The dataclass of user rank
    
    Attributes
    ----------
    number: :class:`int`
        The player's rank as number. Has the value from `1` to `31+N`,
        where `N` is :attr:`legend_number`
        
    legend_number: :class:`int`
        Only if player has `Legend` rank! The number of `Legend` rank"""

    number: int

    @property
    def legend_number(self) -> int:
        """:class:`int`: if the player has the `Legend` rank, then returns
        the number of this rank, otherwise returns `-1`"""
        return -1 if self.number < 31 else self.number-30

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(number={self.number})"

    def __str__(self) -> str:
        return f"Rank #{self.number}"

    def __hash__(self) -> int:
        return hash(self.number)
