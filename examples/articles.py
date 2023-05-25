"""The example of working with eSport articles"""

import asyncio

from toapi import Article, ESportListResponse, get_articles


async def main():
    """The entrypoint of the example"""
    articles: ESportListResponse[Article] = await get_articles()
    print(f"Page #{articles.page} ({articles.per_page} elements per page) of {articles.last_page} pages\n")
    last_article: Article = articles.data[0]
    print("Info about last article (index 0)")
    print(f"  Title: {last_article.title}")
    print(f"  Author: {last_article.author.name} ({last_article.author.id})")
    print(f"  Primary category: {last_article.category.name}")
    print(f"  Image: {last_article.image}")
    print(f"  Created at {last_article.date.strftime('%d.%m.%Y %H:%M:%S')}")

if __name__ == "__main__":
    asyncio.run(main())
