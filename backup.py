from collections import deque, namedtuple
from enum import Enum
from pathlib import Path
from tree import Node, NodeWrapper, Fil, Dir, FileSysTree

class UpdateMethod(Enum):
    ADD = 1
    DEL = 2


class UpdateQuItem:
    def __init__(self, method:UpdateMethod, node: NodeWrapper):
        self.method = method
        self.node = node


def make_tree_update_qu(dir_path:Path, tree:FileSysTree) -> list[UpdateQuItem]:
    """Generate qu of updates to make to make to `tree` based on the comparison beween the nodes in `tree` and `dir_path`."""
    
    # TODO
    return tree

def make_xfer_qu(src:Path, backup_tree:FileSysTree) -> list[Path]:
    """Generate `qu` from `src` and `backup_tree`."""
    qu:list[Path] = list() # ordered list/qu of dirs and files from `src` that are not yet in the backup destination 
    # TODO
    return qu

def xfer(xfer_qu:list[Path], dest:Path) -> list[Path]:
    """Transfer the dir or file from each path in `xfer_qu` (in ascending order) to `dest`.
        Returns `failed_paths` (list of paths for which xfer failed).
    """
    failed_paths:list = list()
    for path in xfer_qu:
        try:
            pass # TODO
        except Exception as e: # TODO
            failed_paths.append(path)
    return failed_paths

def append_to_tree(paths:list[Path], tree:FileSysTree):
    """Append new paths from `path` to `tree`."""
    pass # TODO
