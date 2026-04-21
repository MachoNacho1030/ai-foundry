"""
Tests for file deduplication function.
We write tests FIRST (TDD red step) — they will fail until the solution exists.

Strategy: create temporary files and directories in each test so nothing
leaks onto disk after the test finishes.
"""

import os
import tempfile
import pytest
from solutions.file_deduplication import is_duplicate


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write_file(directory: str, filename: str, content: bytes) -> str:
    """Write bytes to a file inside directory, return the full path."""
    path = os.path.join(directory, filename)
    with open(path, "wb") as f:
        f.write(content)
    return path


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestIsDuplicate:

    def test_exact_duplicate_returns_true(self, tmp_path):
        """
        The incoming file has byte-for-byte identical content to a stored file.
        Should return True — it IS a duplicate.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        # Store a file first
        write_file(str(storage), "existing.txt", b"hello world")

        # Incoming file has the same content
        incoming = write_file(str(tmp_path), "incoming.txt", b"hello world")

        assert is_duplicate(incoming, str(storage)) is True

    def test_unique_file_returns_false(self, tmp_path):
        """
        The incoming file has different content from everything in storage.
        Should return False — it is NOT a duplicate.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        write_file(str(storage), "existing.txt", b"hello world")

        incoming = write_file(str(tmp_path), "incoming.txt", b"something completely different")

        assert is_duplicate(incoming, str(storage)) is False

    def test_empty_storage_dir_returns_false(self, tmp_path):
        """
        Storage directory exists but has no files yet.
        Any upload should be treated as new — return False.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        incoming = write_file(str(tmp_path), "incoming.txt", b"first file ever")

        assert is_duplicate(incoming, str(storage)) is False

    def test_duplicate_detected_among_multiple_files(self, tmp_path):
        """
        Storage has several files. The incoming file matches one of them.
        Should return True even if it doesn't match the others.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        write_file(str(storage), "file_a.txt", b"apple")
        write_file(str(storage), "file_b.txt", b"banana")
        write_file(str(storage), "file_c.txt", b"cherry")  # incoming will match this

        incoming = write_file(str(tmp_path), "incoming.txt", b"cherry")

        assert is_duplicate(incoming, str(storage)) is True

    def test_different_filename_same_content_is_duplicate(self, tmp_path):
        """
        Two files with different names but identical bytes are duplicates.
        The function should not care about the filename at all.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        write_file(str(storage), "report_v1.pdf", b"PDF content bytes")

        # Same bytes, totally different name
        incoming = write_file(str(tmp_path), "report_final_FINAL.pdf", b"PDF content bytes")

        assert is_duplicate(incoming, str(storage)) is True

    def test_same_filename_different_content_is_not_duplicate(self, tmp_path):
        """
        Two files with the same name but different bytes are NOT duplicates.
        Hash is what matters, not the name.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        write_file(str(storage), "data.txt", b"version 1 content")

        incoming = write_file(str(tmp_path), "data.txt", b"version 2 content - totally changed")

        assert is_duplicate(incoming, str(storage)) is False

    def test_empty_file_duplicate(self, tmp_path):
        """
        Two empty files are byte-for-byte identical (both hash to the same value).
        Should return True.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        write_file(str(storage), "empty_stored.txt", b"")

        incoming = write_file(str(tmp_path), "empty_incoming.txt", b"")

        assert is_duplicate(incoming, str(storage)) is True

    def test_large_file_duplicate(self, tmp_path):
        """
        Hashing must work on large files read in chunks — not all at once.
        This test uses a 5MB file to verify chunk-based reading produces the correct result.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        large_content = b"x" * (5 * 1024 * 1024)  # 5 MB of the same byte
        write_file(str(storage), "large.bin", large_content)

        incoming = write_file(str(tmp_path), "large_incoming.bin", large_content)

        assert is_duplicate(incoming, str(storage)) is True

    def test_subdirectories_in_storage_are_ignored(self, tmp_path):
        """
        If storage contains subdirectories, the function must skip them
        (os.path.isfile check) and not crash trying to hash a directory.
        """
        storage = tmp_path / "storage"
        storage.mkdir()

        # Create a subdirectory inside storage — not a file
        subdir = storage / "subdir"
        subdir.mkdir()

        incoming = write_file(str(tmp_path), "incoming.txt", b"some content")

        # Should return False cleanly, not crash
        assert is_duplicate(incoming, str(storage)) is False
