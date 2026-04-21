"""
File Deduplication
==================
Given an incoming file path and a storage directory, return True if the
incoming file is a byte-for-byte duplicate of any file already in storage,
False otherwise.

Approach: SHA-256 hashing
- Read the incoming file in 8 KB chunks and feed each chunk into a SHA-256
  hasher. Do the same for every file in the storage directory.
- Comparing two 64-character hex strings (hashes) is far cheaper than
  comparing millions of raw bytes, and reading in chunks keeps memory usage
  constant regardless of file size.

Time:  O(n * m) where n = number of stored files, m = size of the largest file
Space: O(1) — only one 8 KB buffer in memory at a time
"""

import hashlib
import os


# Size of each chunk we read from disk at a time (8 KB is a common sweet spot
# between too many syscalls and too much memory pressure).
_CHUNK_SIZE = 8192


def _hash_file(path: str) -> str:
    """
    Compute the SHA-256 hash of a file by reading it in fixed-size chunks.

    Reading in chunks (instead of file.read() all at once) means a 5 GB video
    and a 5 byte text file use the same amount of RAM during hashing.

    Returns the hash as a lowercase hex string, e.g.
    'e3b0c44298fc1c149afb...' (64 chars).
    """
    hasher = hashlib.sha256()  # SHA-256 produces a 256-bit fingerprint

    with open(path, "rb") as f:  # open in binary mode — no encoding surprises
        while True:
            chunk = f.read(_CHUNK_SIZE)  # read the next 8 KB slice
            if not chunk:               # empty bytes means we've hit EOF
                break
            hasher.update(chunk)        # feed this slice into the running hash

    return hasher.hexdigest()  # finalize and return as hex string


def is_duplicate(incoming_path: str, storage_dir: str) -> bool:
    """
    Return True if `incoming_path` is a byte-for-byte duplicate of any file
    currently in `storage_dir`, False otherwise.

    Args:
        incoming_path: Absolute or relative path to the file being uploaded.
        storage_dir:   Path to the directory holding already-stored files.

    How it works:
    1. Hash the incoming file once.
    2. Walk every entry in storage_dir.
    3. Skip subdirectories (they can't be hashed like files).
    4. Hash each stored file and compare to the incoming hash.
    5. Return True on the first match; return False if no match found.
    """
    # Step 1: get the fingerprint of the file we're checking
    incoming_hash = _hash_file(incoming_path)

    # Step 2: compare against every file in storage
    for entry in os.listdir(storage_dir):
        stored_path = os.path.join(storage_dir, entry)  # build the full path

        # Step 3: skip subdirectories — os.listdir returns both files and dirs
        if not os.path.isfile(stored_path):
            continue

        # Step 4: hash the stored file and compare fingerprints
        stored_hash = _hash_file(stored_path)

        if stored_hash == incoming_hash:
            return True  # found a match — it's a duplicate

    # Step 5: no match found after checking everything
    return False
