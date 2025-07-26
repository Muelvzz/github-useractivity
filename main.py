import os
import hashlib
import pickle

def read_file(path):
    """Read contents of file at given path as bytes."""
    with open(path, 'rb') as f:
        return f.read()


def write_file(path, data):
    """Write data bytes to file at given path."""
    with open(path, 'wb') as f:
        f.write(data)

def init_vcs(get_repo):
    """ Creates a hidden folder in the current working directory and initializes git."""
    os.makedirs(get_repo, exist_ok=True)
    os.makedirs(os.path.join(get_repo, ".git"), exist_ok=True)

    for name in ["objects", "refs", "refs/heads"]:
        os.makedirs(os.path.join(get_repo, ".git", name), exist_ok=True)

    write_file(os.path.join(get_repo, ".git", "HEAD"), b'ref: refs/heads/master')
    print("Git initialized {}".format(get_repo))