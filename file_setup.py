import os

paths = ["/etc/passwd", "/etc/group"]


def get_file_to_read(path: str, task: int):
    if os.path.exists(path):
        return open(path, "r")
    elif os.path.exists(paths[task]):
        print("File at ", path, " does not exist")
        return open(paths[task], "r")
    else:
        print("File at ", paths[task], " does not exist")
