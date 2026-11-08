from datetime import datetime
from pathlib import Path
from typing import Self

class SameFilNameException(Exception): pass
class SameDirNameException(Exception): pass


class Node:
    def __init__(self, name:str, last_modified:datetime):
        self.name:str = str(name)
        self.last_modified:datetime = last_modified

    def __str__(self):
        return self.name


class NodeWrapper:
    def __init__(self, node:Node|None=None, path:Path|None=None):
        self.node = node
        self.path = path


class Fil(Node):
    pass


class Dir(Node):
    def __init__(self, dirs:dict[str,Self]=dict(), fils:set[Fil]=set()):
        self.dirs = dirs
        self.fils = fils

    def add_fil(self, fil:Fil):
        """Add item to `fils`."""
        if(not isinstance(fil, Fil)):
            raise TypeError(f"fil is {type(fil)}")
        elif (fil.name in self.fils):
            raise SameFilNameException(f"'{fil.name}' preexists in {self.name}")
        
        self.fils.add(fil)

    def add_dir(self, dir:Self):
        """Add item to `dirs`."""
        if(not isinstance(dir, Dir)):
            raise TypeError(f"dir is {type(dir)}")
        
        elif(dir.name in self.dirs.keys()):
            raise SameDirNameException(f"'{dir.name}' preexists in {self.name}")
        
        self.dirs[dir.name] = dir

    def add(self, node:Node):
        """Add file or directory item."""
        if(isinstance(node, Fil)):
            self.add_fil(node)
        elif(isinstance(node, Dir)):
            self.add_dir(node)
        
        else:
            raise TypeError(f"node is {type(node)}")


class FileSysTree:
    def __init__(self, root:Node|None=None):
        self.root = root
        self.cursor = self.root
