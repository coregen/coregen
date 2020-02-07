import os
from contextlib import contextmanager


def same_paths(*paths):
    resolved_paths = [os.path.abspath(path) for path in paths]
    first_path, *rest_paths = resolved_paths
    return all(path == first_path for path in rest_paths)


@contextmanager
def enter_directory_ctx(directory):
    current_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(current_directory)


def flatten_2d_list(l):
    return [sub_item for item in l for sub_item in item]
