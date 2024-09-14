# test_file_io.py

import pytest
from lib.file_io import write_file, append_file, read_file

def test_write_file(tmp_path):
    """Test write_file()"""
    file_path = tmp_path / "test_file"
    file_content = "This is a test content."
    write_file(file_path, file_content)
    with open(f'{file_path}.txt', 'r') as f:
        assert f.read() == file_content

def test_append_file(tmp_path):
    """Test append_file()"""
    file_path = tmp_path / "test_file"
    file_content = "This is a test content."
    append_content = "Appended content."
    write_file(file_path, file_content)
    append_file(file_path, "\n" + append_content)  # Add newline before appending
    with open(f'{file_path}.txt', 'r') as f:
        file_content_read = f.read()
    expected_content = file_content + "\n" + append_content  # Adjust expected content
    assert file_content_read == expected_content

def test_read_file(tmp_path):
    """Test read_file()"""
    file_path = tmp_path / "test_file"
    write_file(file_path, "Reading content.")
    assert read_file(file_path) == "Reading content.\n"
