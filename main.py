import os
import hashlib
import pickle

def init_vcs():
    """ Creates a hidden folder in the current working directory"""
    os.makedirs(".vcs_storage", exist_ok=True)
    print("VCS Initialized")

def snapshot(get_directory="."):  # Default to current directory
    """ Generating Hash or like a fingerprint in a directory """
    snapshot_hash = hashlib.sha256()
    snapshot_data = {"files" : {}}

    # Looping over files in the directory
    for root, dirs, files in os.walk(get_directory):
        for file in files:
            if ".vcs_storage" in os.path.join(root, file):
                continue

            file_path = os.path.join(root, file)

            with open(file_path, "rb") as f:
                content = f.read()
                snapshot_hash.update(content)
                snapshot_data["files"][file_path] = content

    hash_digest = snapshot_hash.hexdigest()
    snapshot_data["file_list"] = list(snapshot_data["files"].keys())

    with open(f".vcs_storage/{hash_digest}", "wb") as f:
        pickle.dump(snapshot_data, f)

    print(f"Snapshot created with {hash_digest}")

def revert_to_snapshot(get_hash_digest):
    snapshot_path = f".vcs_storage/{get_hash_digest}"

    if not os.path.exists(snapshot_path):
        print("Snapshot does not exist")
        return
    
    with open(snapshot_path, "rb") as f:
        snapshot_data = pickle.load(f)  # Fixed variable name

    # Restore all files from snapshot
    for file_path, content in snapshot_data["files"].items():  # Fixed variable name
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(content)

    # Find current files in directory
    current_files = set()
    for root, dirs, files in os.walk(".", topdown=True):  # Fixed: "." instead of ","
        if ".vcs_storage" in root:
            continue
        for file in files:
            current_files.add(os.path.join(root, file))

    # Delete files that shouldn't exist
    snapshot_files = set(snapshot_data["file_list"])
    files_to_delete = current_files - snapshot_files

    for file_path in files_to_delete:
        os.remove(file_path)
        print(f"Removed {file_path}")

    print(f"Reverted to snapshot {get_hash_digest}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python vcs.py <command> [arguments]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == "init":
        init_vcs()
    elif command == "snapshot":
        if len(sys.argv) > 2:
            snapshot(sys.argv[2])  # Use provided directory
        else:
            snapshot()  # Use current directory
    elif command == "revert":
        if len(sys.argv) < 3:
            print("Please provide a hash digest")
            sys.exit(1)
        revert_to_snapshot(sys.argv[2])  # Pass the hash argument
    else:
        print("Unknown command. Available commands: init, snapshot, revert")