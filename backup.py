from collections import deque
from pathlib import Path
from tree import Tree

def make_backup_tree(backup_dir) -> Tree:
    """Generate `tree` from `backup_dir`."""
    tree = Tree()
    # TODO
    return tree

def make_xfer_qu(src:Path, backup_tree:Tree) -> list[Path]:
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

def append_to_tree(paths:list[Path], tree:Tree):
    """Append new paths from `path` to `tree`."""
    pass # TODO

def run(src:Path, dest:Path, tree:Tree):
    # read contents of
    src_cursor:deque = deque([src.name])
    # TODO
