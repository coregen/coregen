import os

from coregen.common import flatten_2d_list


def top_level_dirs_from_path(path):
    for _, dirs, _ in os.walk(path):
        return dirs


def top_level_dirs_from_iter(paths):
    paths_nested = [top_level_dirs_from_path(path=path) for path in paths]
    return flatten_2d_list(paths_nested)


class TopLevelDirIter:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        if isinstance(self.path, str):
            return (d for d in top_level_dirs_from_path(self.path))
        elif isinstance(self.path, list):
            return (d for d in top_level_dirs_from_iter(self.path))
