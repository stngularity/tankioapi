"""Copyright 2023-present stngularity

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from dataclasses import dataclass
from typing import Any, List, Mapping, Optional, Tuple, Type

__all__ = ("StableServerStatus", "StableServerNode")


@dataclass
class StableServerStatus:
    """The dataclass for stable Tanki Online server

    Maybe deprecated. I don't know this. Judging by the content of the
    response from the API, the chance of this is approximately `99%`
    
    Attributes
    ----------
    apk_link: Optional[:class:`str`]
        The link (URL) for download APK of this game
        
    supported_android: Tuple[:class:`int`, ...]
        The tuple with min and max supported Android versions
        
    nodes: List[:class:`StableServerNode`]
        The list with nodes of the server"""

    apk_link: Optional[str]
    supported_android: Tuple[int, ...]
    nodes: List["StableServerNode"]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(apk_link={self.apk_link}; {len(self.nodes)} nodes)"

    def __str__(self) -> str:
        return f"{len(self.nodes)} nodes"

    def __hash__(self) -> int:
        return hash(len(self.nodes))

    @classmethod
    def from_json(cls: Type["StableServerStatus"], data: Mapping[str, Any]) -> "StableServerStatus":
        """:class:`StableServerStatus`: Converts JSON data to :class:`StableServerStatus`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The JSON data"""
        self = cls.__new__(cls)
        self.apk_link = data["linkForDownloadAPK"] or None
        self.supported_android = (data["minSupportedAndroidVersion"], data["maxSupportedAndroidVersion"])
        self.nodes = [StableServerNode.from_json(v, name=k) for k, v in data["nodes"].items()]
        return self

@dataclass
class StableServerNode:
    """The dataclass for nodes of stable Tanki Online server
    
    Maybe deprecated. I don't know this. Judging by the content of the
    response from the API, the chance of this is approximately `99%`
    
    Attributes
    ----------
    name: :class:`str`
        The name of the node
        
    host: :class:`str`
        The hostname of the node
        
    status: :class:`str`
        The status of the node
        
    tcp_ports: Tuple[:class:`int`, ...]
        The tuple with all `TCP` ports of the node
        
    ws_ports: Tuple[:class:`int`, ...]
        The tuple with all `WebSocket` ports of the node
        
    inbattles: :class:`int`
        The count of player which in a battle now
        
    online: :class:`int`
        The count of player which online now
        
    partners: Mapping[:class:`str`, :class:`Any`]
        I don't know what is.... Sorry"""

    name: str
    host: str
    status: str
    tcp_ports: Tuple[int, ...]
    ws_ports: Tuple[int, ...]
    inbattles: int
    online: int
    partners: Mapping[str, Any]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name=\"{self.name}\" host=\"{self.host}\")"

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    @classmethod
    def from_json(cls: Type["StableServerNode"], data: Mapping[str, Any], *, name: str) -> "StableServerNode":
        """:class:`StableServerNode`: Converts JSON data to :class:`StableServerNode`
        
        Parameters
        ----------
        data: Mapping[:class:`str`, :class:`Any`]
            The JSON data
            
        name: :class:`str`
            The name of the node"""
        self = cls.__new__(cls)
        self.name = name
        self.host = data["endpoint"]["host"]
        self.status = data["endpoint"]["status"]
        self.tcp_ports = tuple(data["endpoint"]["tcpPorts"])
        self.ws_ports = tuple(data["endpoint"]["wsPorts"])
        self.inbattles = data["inbattles"]
        self.online = data["online"]
        self.partners = data["partners"]
        return self
