"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

# pylint: disable=C0103

from typing import Any, List, Mapping

from .errors import TankiOnlineException, UserNotFoundError
from .http import request
from .types import Article, ArticleComment, ESportListResponse, StableServerStatus, TestServerStatus, TopLists, User

__all__ = ("get_tops", "get_user", "get_status", "get_test_status", "get_articles", "get_article_info",
           "get_article_comments")


async def get_tops() -> TopLists:
    """List[:class:`Top`]: Gets list with tops of players
    
    Raises
    ------
    :class:`TankiOnlineException`
        If the response from the API says that the operation wasn't successful"""
    response: Mapping[str, Any] = await request("GET", "/top")
    if response["responseType"] != "OK":
        raise TankiOnlineException("Failed to get the tops")

    return TopLists.from_json(response["response"])


async def get_user(name: str, *, lang: str = "en") -> User:
    """:class:`User`: Tries to find user by the name

    Parameters
    ----------
    name: :class:`str`
        The name of the user

    lang: :class:`str`
        The language of API response. By default, `en`
    
    Raises
    ------
    :class:`UserNotFoundError`
        If user with specified :param:`name` isn't found. This error is
        possible if a player with such a name doesn't exist, or he
        disables the ability to receive information about him through
        the API"""
    response: Mapping[str, Any] = await request("GET", f"/profile?user={name}&lang={lang}")
    if response["responseType"] == "NOT_FOUND":
        raise UserNotFoundError(name, f"Failed to find player with \"{name}\" name")

    return User.from_json(response["response"])


async def get_status() -> StableServerStatus:
    """:class:`StableServerStatus`: Gets the status of stable game server.
    
    Maybe deprecated. I don't know this. Judging by the content of the
    response from the API, the chance of this is approximately `99%`"""
    response: Mapping[str, Any] = await request("GET", "/status.js", base="https://tankionline.com/s")
    return StableServerStatus.from_json(response)


async def get_test_status() -> List[TestServerStatus]:
    """List[:class:`TestServerStatus`]: Gets the status of test game servers"""
    response: List[Mapping[str, Any]] = await request("GET", "/public_test", base="https://test.tankionline.com")

    output: List[TestServerStatus] = []
    for server in response:
        base: str = f"https://balancer.{server['Domain']}"
        nodes: Mapping[str, Mapping[str, Any]] = (await request("GET", "/balancer", base=base))["nodes"]
        output.append(TestServerStatus.from_json(server, nodes))

    return output


async def get_articles(*, count: int = 20, page: int = 1) -> ESportListResponse[Article]:
    """:class:`ESportListResponse`[:class:`Article`]: Tries to get list of eSport articles
    
    Parameters
    ----------
    count: :class:`int`
        The number of articles per page. Must be more than zero. By default, `20`

    page: :class:`int`
        The number of current page. Must be more than zero. By default, `1`
    
    Raises
    ------
    :class:`ValueError`
        If :param:`count` or :param:`page` less than or equal to zero (`0`)
        
    :class:`TankiOnlineException`
        If the response from the API says that the operation wasn't successful"""
    if count < 1:
        raise ValueError("Value of \"count\" parameter must be more than 0")

    if page < 1:
        raise ValueError("Value of \"page\" parameter must be more than 0")

    endpoint: str = f"/articles?count={count}&page={page}"
    response: Mapping[str, Any] = await request("GET", endpoint, base="https://tankisport.com/api")
    if not response.get("success", False):
        raise TankiOnlineException("Failed to get articles")

    output: List[Article] = [Article.from_json(a) for a in response["data"]["articles"]]
    meta: Mapping[str, Any] = response["meta"]
    return ESportListResponse(output, page=page, last_page=meta["last_page"], per_page=count, total=meta["total"])


async def get_article_info(id: int) -> Article:
    """:class:`Article`: Tries to get information about article with specified ID
    
    Parameters
    ----------
    id: :class:`int`
        ID of the article you want to get information about. For example, You can
        specify ID of last article from response of :func:`get_articles` function
    
    Raises
    ------
    :class:`TankiOnlineException`
        If the response from the API says that the operation wasn't successful"""
    endpoint: str = f"/articles/show/{id}"
    response: Mapping[str, Any] = await request("GET", endpoint, base="https://tankisport.com/api")
    if not response.get("success", False):
        raise TankiOnlineException(f"Failed to get info about article with {id} id")

    return Article.from_json(response["data"])


async def get_article_comments(article_id: int) -> List[ArticleComment]:
    """List[:class:`ArticleComment`]: Tries to get comments of article with
    specified ID
    
    Parameters
    ----------
    article_id: :class:`int`
        ID of the article you want to get comments of. For example, You can specify
        ID of last article from response of :func:`get_articles` function
    
    Raises
    ------
    :class:`TankiOnlineException`
        If the response from the API says that the operation wasn't successful"""
    endpoint: str = f"/comments?article_id={article_id}"
    response: Mapping[str, Any] = await request("GET", endpoint, base="https://tankisport.com/api")
    if not response.get("success", False):
        raise TankiOnlineException(f"Failed to get comments of article with {article_id} id")

    return [ArticleComment.from_json(c) for c in response["data"]]
