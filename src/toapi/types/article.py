"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

# pylint: disable=C0103

from dataclasses import dataclass
from datetime import datetime as dt
from typing import Any, List, Mapping, Optional, Type

__all__ = ("Article", "ArticleAuthor", "ArticleCategory", "ArticleComment")


@dataclass
class Article:
    """The dataclass for articles
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the article

    author: :class:`ArticleAuthor`
        The author of the article

    views: :class:`int`
        The count of article's views

    category: :class:`ArticleCategory`
        The primary category of the article

    categories: Optional[List[:class:`ArticleCategory`]]
        The array with all categories of the article. If isn't provided by API,
        then it's `None`
        
    title: :class:`str`
        The title (in ``HTML`` format) of the article
        
    short_desc: :class:`str`
        The short description (in ``HTML`` format) of the article

    image: Optional[:class:`str`]
        URL to cover of article. If it isn't specified by article author, then
        it's `None`

    wide_image: Optional[:class:`str`]
        URL to wide image of article. If it isn't specified by article author,
        then it's `None`

    status: :class:`int`
        The status of the article

    type: :class:`int`
        The type of the article

    date: :class:`datetime`
        The exact date and time the article was created
        
    list_order: :class:`int`
        The serial number of the article in the list of articles
        
    content: Optional[:class:`str`]
        The content (in ``HTML`` format) of the article. If isn't provided by API,
        then it's `None`
        
    comments: Optional[List[:class:`ArticleComment`]]
        The array with comments at the article. If isn't provided by API, then
        it's `None`"""

    id: int
    author: "ArticleAuthor"
    views: int
    category: "ArticleCategory"
    categories: Optional[List["ArticleCategory"]]
    title: str
    short_desc: str
    image: Optional[str]
    wide_image: Optional[str]
    status: int
    type: int
    date: dt
    list_order: int
    content: Optional[str]
    comments: Optional[List["ArticleComment"]]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, author={self.author}, title={self.title!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.title

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Article) and other.id == self.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @classmethod
    def from_json(cls: Type["Article"], data: Mapping[str, Any]) -> "Article":
        """:class:`Article`: Converts JSON to :class:`Article`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The original data of article"""
        self = cls.__new__(cls)
        self.id = data["id"]
        self.author = ArticleAuthor(id=data["author_id"], name=data["author_username"])
        self.views = data["views"]
        self.category = ArticleCategory.from_json(data["category"][0])

        categories: Optional[List[Mapping[str, Any]]] = data.get("categories")
        self.categories = None if categories is None else [ArticleCategory.from_json(c) for c in categories]

        self.title = data["title"]
        self.short_desc = data["short_desc"]
        self.image = data["image"]
        self.wide_image = data["wide_image"]
        self.status = data["status"]
        self.type = data["type"]
        self.date = dt.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
        self.list_order = data["list_order"]
        self.content = data["content"]

        comments: Optional[List[Mapping[str, Any]]] = data.get("comments")
        self.comments = None if comments is None else [ArticleComment.from_json(c) for c in comments]
        return self


@dataclass
class ArticleAuthor:
    """The dataclass for author of the article
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the author
        
    name: :class:`str`
        The name of the author"""

    id: int
    name: str

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ArticleAuthor) and other.id == self.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)


@dataclass
class ArticleCategory:
    """The dataclass for categories of the article
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the category
        
    name: :class:`str`
        The name of the category
        
    lang: :class:`str`
        2-character code of the language in which the name of the category is
        written. For example, `EN` (i.e. English)
        
    sort_order: Optional[:class:`int`]
        The sort order of the category. From the smallest to the largest
        
    status: Optional[:class:`int`]
        The status of the category"""

    id: int
    name: str
    lang: str
    sort_order: Optional[int]
    status: Optional[int]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, lang={self.lang!r})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ArticleCategory) and other.id == self.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @classmethod
    def from_json(cls: Type["ArticleCategory"], data: Mapping[str, Any]) -> "ArticleCategory":
        """:class:`ArticleCategory`: Converts JSON to :class:`ArticleCategory`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The original data of category"""
        self = cls.__new__(cls)
        self.id = data["id"]
        self.name = data["name"]
        self.lang = data["lang"]
        self.sort_order = data.get("sort_order")
        self.status = data.get("status")
        return self


@dataclass
class ArticleComment:
    """The dataclass for comments at articles
    
    Attributes
    ----------
    id: :class:`int`
        The ID of the comment
        
    commentable_type: :class:`str`
        The type of article at which the comment is sent
        
    commentable_id: :class:`int`
        The ID of article at which the comment is sent
        
    parent_id: Optional[:class:`int`]
        The ID of the comment that the comment is responding to. If the comment
        doesn't respond to another comment, then it's `None`
        
    text: :class:`str`
        The text content (in ``HTML`` format) of the comment
        
    is_approved: :class:`bool`
        Whether the comment approved by moderation
        
    user_id: :class:`int`
        The ID of the user that sent the comment
        
    created_at: :class:`datetime`
        The exact date and time the comment was created
        
    updated_at: :class:`datetime`
        The exact date and time the comment was updated"""

    id: int
    commentable_type: str
    commentable_id: int
    parent_id: Optional[int]
    text: str
    is_approved: bool
    user_id: int
    created_at: dt
    updated_at: dt

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, text={self.text!r}, user_id={self.user_id})"

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return self.text

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ArticleComment) and other.id == self.id

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @classmethod
    def from_json(cls: Type["ArticleComment"], data: Mapping[str, Any]) -> "ArticleComment":
        """:class:`ArticleComment`: Converts JSON to :class:`ArticleComment`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The original data of comment"""
        self = cls.__new__(cls)
        self.id = data["id"]
        self.commentable_type = data["commentable_type"]
        self.commentable_id = data["commentable_id"]
        self.parent_id = data["parent_id"]
        self.text = data["comment"]
        self.is_approved = data["is_approved"] == 1
        self.user_id = data["user_id"]
        self.created_at = dt.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        self.updated_at = dt.strptime(data["updated_at"], "%Y-%m-%d %H:%M:%S")
        return self
