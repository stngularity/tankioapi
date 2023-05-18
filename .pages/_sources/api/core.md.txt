```{currentmodule} toapi
```

# Core API
The basic functions of the library are described here.

## ``get_tops``
```{eval-rst}
.. autofunction:: get_tops
```

Gets and returns the tops of players.
- Top by **count of earned by crystals:** ``TopLists.crystals``
- Top by **efficiency:** ``TopLists.efficiency``
- Top by **count of caught golds:** ``TopLists.golds``
- Top by **score:** ``TopLists.score``

<h6>Usage</h6>

```py
tops: TopLists = await toapi.get_tops()
```

<h6>Example</h6>

::::{tab-set}
:::{tab-item} Input
```py
import asyncio
from toapi import Top, TopLists, get_tops

tops: TopLists = asyncio.run(get_tops())
efficiency_top: Top = tops.efficiency
print("----- Efficiency top -----")
for number, user in enumerate(efficiency_top.users):
    print(f"#{number+1}   {user.name} ({user.top_value})")
```

[Full example located at GitHub.](https://github.com/stngularity/tankioapi/blob/main/examples/top.py)
:::
:::{tab-item} Output

```py
#1   TOP1USERNAME (TOP1VALUE)
#2   TOP2USERNAME (TOP2VALUE)
#3   TOP3USERNAME (TOP3VALUE)
...
```
:::
::::

## ``get_user``
```{eval-rst}
.. autofunction:: get_user
```

Tries to find user by specified name.

<h6>Usage</h6>

```py
user: User = await get_user("USERNAME HERE")

# You can specify the language of API response,
# for doing this use "lang" parameter.
user: User = await get_user("USERNAME HERE", lang="ru")
```

<h6>Example</h6>

::::{tab-set}
:::{tab-item} Input
```py
import asyncio
from toapi import User, get_user

user: User = asyncio.run(get_user("sty"))
# and You can specify language
# user: User = asyncio.run(get_user("sty", lang="ru"))

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

[Full example located at GitHub.](https://github.com/stngularity/tankioapi/blob/main/examples/user_info.py)
:::
:::{tab-item} Output

```py
Name: sty
Rank: Warrant Officer 1 (57010/76000 75%)
Has premium: No

KD: 611/398 (1.54)
Caught golds: 0
Crystals: 17416
GS: 3238
```

This data is correct as of May 18, 2023.
:::
::::

## ``get_status``
```{eval-rst}
.. autofunction:: get_status
```

Gets and returns the status of stable game server.

:::{warning}
Maybe deprecated. I don't know this. Judging by the content of the response from the
API, the chance of this is approximately **99%**
:::

<h6>Usage</h6>

```py
status: StableServerStatus = await get_status()
```

<h6>Example</h6>

::::{tab-set}
:::{tab-item} Input
```py
import asyncio
from toapi import StableServerStatus, get_status

status: StableServerStatus = asyncio.run(get_status())
print(f"{len(status.nodes)} nodes")
```
:::
:::{tab-item} Output

```py
8 nodes
```

This data is correct as of May 18, 2023.
:::
::::

## ``get_test_status``
```{eval-rst}
.. autofunction:: get_test_status
```

Gets and returns the status of test game servers

<h6>Usage</h6>

```py
servers: List[TestServerStatus] = await get_test_status()
```

<h6>Example</h6>

::::{tab-set}
:::{tab-item} Input
```py
import asyncio
from typing import List
from toapi import TestServerStatus, get_test_status

servers: List[TestServerStatus] = asyncio.run(get_test_status())
print(f"Total {len(servers)} test servers\n")
for server in servers:
    print(f"{server.release}: {server.domain}; {server.user_count} users and {len(server.nodes)} nodes")
```

[Full example located at GitHub.](https://github.com/stngularity/tankioapi/blob/main/examples/test_server_info.py)
:::
:::{tab-item} Output

```py
Total 3 test servers

deploy1-pubto: public-deploy1.test-eu.tankionline.com; 73 users and 2 nodes
deploy4-pubto: public-deploy4.test-eu.tankionline.com; 4 users and 2 nodes 
deploy6-pubto: public-deploy6.test-eu.tankionline.com; 1 users and 2 nodes 
```

This data is correct as of May 18, 2023.
:::
::::