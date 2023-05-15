<p align=center>
    <img src="https://img.shields.io/badge/-stngularity's%20work-%2346df11">
    <img src="https://img.shields.io/pypi/v/tankioapi?color=%2346df11&label=Version">
    <img src="https://img.shields.io/pypi/dd/tankioapi?color=%2346df11&label=Downloads">
</p>
<p align=center>
    <img src="https://img.shields.io/github/issues/stngularity/tankioapi?color=%2346df11&label=Issues">
    <img src="https://img.shields.io/github/license/stngularity/tankioapi?color=%2346df11&label=License">
</p>

## Notification
This project was created just to exist. Of course, I will update it when the API itself changes, but not immediately. Well, if You want to support this project, You can give it a star.

## Information
As mentioned earlier, this project is created just to exist. And so, the module itself is needed to get the top of players and get information about the player separately. If You know more functionality of the API of the game `Tanki Online`, then please report this functionality in the [`Issues`](https://github.com/stngularity/tankioapi/issues).

###### Features
- Fully `async`/`await`
- Getting top of players
- Getting information of any player by him name
- Getting status of stable server ` Maybe deprecated `

## Installing
**[Python 3.8](https://www.python.org/downloads/) or higher is required**

To install a non-`speedup` version of the library, do the following:
> ```sh
> # Linux/macOS
> python3 -m pip install -U tankioapi
>
> # Windows
> py -3 -m pip install -U tankioapi
> ```

Or, to install the `speedup` version, do the following:
> ```sh
> # Linux/macOS
> python3 -m pip install -U "tankioapi[speedup]"
>
> # Windows
> py -3 -m pip install -U tankioapi[speedup]
> ```

And, to install the development version, do the following:
> ```sh
> $ git clone https://github.com/stngularity/tankioapi
> $ cd tankioapi
> $ python3 -m pip install -U .[speedup]
> ```

## Examples
Here are examples of some of the features of the library. More examples in [`examples/`](/examples)

###### Getting all tops of players
```py
import asyncio
from toapi import Top, TopLists, get_tops


tops: TopLists = asyncio.run(get_tops())
efficiency_top: Top = tops.efficiency
print("----- Efficiency top -----")
for number, user in enumerate(efficiency_top.users):
    print(f"#{number+1}   {user.name} ({user.top_value})")
```

###### Getting information of player
```py
import asyncio
from toapi import User, get_user

user = asyncio.run(get_user("sty"))
# and You can specify language
# user = asyncio.run(get_user("sty", lang="ru"))

print(f"Name: {user.name}")
rank: str = user.rank.name.title()
print(f"Rank: {rank} ({user.score}/{user.score_next} {round(user.score/user.score_next*100)}%)")
print(f"Has premium: {'Yes' if user.premium else 'No'}")
print()
print(f"KD: {user.kills}/{user.deaths} ({user.kd_ratio})")
print(f"Caught golds: {user.caught_golds}")
print(f"Crystals: {user.crystals}")
print(f"GS: {user.gear_score}")
```

## License
This project is distributed under the `MIT` license. You can learn more from the [**LICENSE**](/LICENSE) file.