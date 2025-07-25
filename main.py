import os
import hashlib
import pickle

def init_vcs():

    """ Creates a hidden folder in the current working directory"""

    os.makedirs(".vcs_storage", exist_ok=True)
    print("VCS Initialized")

def snapshot(get_directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {"file" : {}}

    for root, dirs, files in os.walk(get_directory):
        for file in files:
            if ".vcs_storage" in os.path.join(root, file):
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "rb") as f:
                content = f.read()
                snapshot_hash.update(content)
                snapshot_data['file'][file_path] = content