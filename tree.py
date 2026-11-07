from datetime import datetime

class Node:
    def __init__(self, name:str, last_modified:datetime):
        self.name = name
        self.last_modified = last_modified

class Fil(Node):
    pass

class Dir(Node):
    def __init__(self, contents:dict[Node|None]):
        pass

class Tree:
    def __init__(self, root:Node|None=None):
        self.root = root
