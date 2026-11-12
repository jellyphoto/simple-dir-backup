from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Optional


class SameFilNameException(Exception): pass
class SameDirNameException(Exception): pass


class Node:
    def __init__(self, name:str, last_modified:datetime):
        self.name:str = name
        self.last_modified:datetime = last_modified

    def __str__(self) -> str:
        return self.name


class NodeWrapper:
    def __init__(self, node:Node, path:Path):
        self.node:Node = node
        self.path:Path = path


class Fil(Node):
    pass


class Dir(Node):
    def __init__(self, dirs:Optional[dict[str,Dir]]=None, fils:Optional[set[Fil]]=None):
        self.dirs: dict[str, Dir] = dict() if dirs is None else dirs
        self.fils: set[Fil] = set() if fils is None else fils

    def add_fil(self, fil:Fil) -> None:
        """Add item to `fils`."""
        if (fil.name in self.fils):
            raise SameFilNameException(f"'{fil.name}' preexists in {self.name}")        
        self.fils.add(fil)

    def add_dir(self, dir:Dir) -> None:
        """Add item to `dirs`."""       
        if(dir.name in self.dirs.keys()):
            raise SameDirNameException(f"'{dir.name}' preexists in {self.name}")
        
        self.dirs[dir.name] = dir

    def add(self, node:Node) -> None:
        """Add file or directory item."""
        if(isinstance(node, Dir)):
            self.add_dir(node)
        elif(isinstance(node, Fil)):
            self.add_fil(node)
        else:
            raise TypeError(f"type(node) = {type(node)}")


class FileSysTree:
    def __init__(self, root:Optional[Node]=None):
        self.root: Optional[Node] = root
        self.cursor = self.root
