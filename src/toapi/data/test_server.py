"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from typing import Final, Optional

__all__ = ("build_test_url",)


TEST_URL: Final[str] = "https://{domain}/{type}/index.html?"
HTML5: Final[str] = "config-template=https://c{{server}}.{domain}/config.xml&resources=../resources&balancer=https://balancer.{domain}/balancer"
FLASH: Final[str] = "config=https://c1.{domain}/config.xml&locale={lang}&lang={lang}"


def build_test_url(type: str, *, domain: str, lang: Optional[str] = None) -> str:
    """:class:`str`: Builds URL to Tanki Online test server
    
    Parameters
    ----------
    type: :class:`str`
        The type of the URL. Must have value of `html` or `flash`
        
    domain: :class:`str`
        The domain of test server release
        
    lang: Optional[:class:`str`]
        The language of `flash`-type URL. Requires if :param:`type` have
        `flash` value, otherwise ignored. By default, `None`
        
    Raises
    ------
    :class:`ValueError`
        If :param:`type` have invalid value or :param:`type` have `flash`
        value but :param:`lang` isn't specified"""
    if type not in ["html", "flash"]:
        raise ValueError("\"type\" must have value of \"html\" or \"flash\"")

    if type == "flash" and lang is None:
        raise ValueError("You must specify \"lang\" argument")

    url: str = TEST_URL + (HTML5 if type == "html" else FLASH)
    return url.format(domain=domain, lang=lang, type=type)
