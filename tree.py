from datetime import datetime
from pathlib import Path

class SameNameNodeExists(Exception): pass

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
    def __init__(self, contents:dict[str,Node|None]):
        self.contents = contents

    def add(self, item:Node):
        if (item.name in self.contents.keys()):
            raise SameNameNodeExists(item.name)
        
        self.contents[item.name] = item

class FileSysTree:
    def __init__(self, root:Node|None=None):
        self.root = root
        self.cursor = self.root
