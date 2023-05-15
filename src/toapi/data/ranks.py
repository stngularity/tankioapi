"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import locale
from typing import Final, List

__all__ = ("get_rank_name",)


LANG_EN: Final[List[str]] = ["recruit", "private", "gefreiter", "corporal", "master corporal", "sergeant",
                             "staff sergeant", "master sergeant", "first sergeant", "sergeant-major",
                             "warrant officer 1", "warrant officer 2", "warrant officer 3", "warrant officer 4",
                             "warrant officer 5", "third lieutenant", "second lieutenant", "first lieutenant",
                             "captain", "major", "lieutenant colonel", "colonel", "brigadier", "major general",
                             "lieutenant general", "general", "marshal", "field marshal", "commander", "generalissimo",
                             "legend"]

LANG_RU: Final[List[str]] = ["новобранец", "рядовой", "ефрейтор", "капрал", "мастер-капрал", "сержант", "штаб-сержант",
                             "мастер-сержант", "первый сержант", "сержант-майор", "уорэнт-офицер 1", "уорэнт-офицер 2",
                             "уорэнт-офицер 3", "уорэнт-офицер 4", "уорэнт-офицер 5", "младший лейтенант", "лейтенант",
                             "старший лейтенант", "капитан", "майор", "подполковник", "полковник", "бригадир",
                             "генерал-майор", "генерал-лейтенант", "генерал", "маршал", "фельдмаршал", "командор",
                             "генералиссимус", "легенда"]


def get_rank_name(rank: int) -> str:
    """:class:`str`: Gets the name of player's rank
    
    Parameters
    ----------
    rank: :class:`int`
        The number of player's rank"""
    index: int = min(rank-1, 30)
    if locale.getlocale()[0] == "Russian_Russia":
        return LANG_RU[index] + ("" if index < 30 else f" {rank-30}")

    return LANG_EN[index] + ("" if index < 30 else f" {rank-30}")
