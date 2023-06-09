"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass
from typing import Generic, List, TypeVar

__all__ = ("ESportListResponse",)

T = TypeVar('T')


@dataclass
class ESportListResponse(Generic[T]):
    """The dataclass for multi-page responses from Tanki Sport API
    
    Attributes
    ----------
    data: List[:class:`Any`]
        The list with elements of API response
        
    page: :class:`int`
        Number of current page in pagination
        
    last_page: :class:`int`
        Number of last page in pagination
        
    per_page: :class:`int`
        Number of elements per pagination page
        
    total: :class:`int`
        Total number of elements in pagination"""

    data: List[T]
    page: int
    last_page: int
    per_page: int
    total: int
