from datetime import datetime

class SameNameNodeExists(Exception): pass

class Node:
    def __init__(self, name:str, last_modified:datetime):
        self.name:str = str(name)
        self.last_modified:datetime = last_modified

    def __str__(self):
        return self.name

class Fil(Node):
    pass

class Dir(Node):
    def __init__(self, contents:dict[str,Node|None]):
        self.contents = contents

    def add(self, item:Node):
        if (item.name in self.contents.keys()):
            raise SameNameNodeExists(item.name)
        
        self.contents[item.name] = item

class Tree:
    def __init__(self, root:Node|None=None):
        self.root = root
        self.cursor = self.root
