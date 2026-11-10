from pathlib import Path
import pytest
from src.file_reader import read_file


def test_reads_file_content(tmp_path):
    file_path = tmp_path / "sample.py"
    expected = "print('Hello ReviewBot')"

    file_path.write_text(expected)

    actual = read_file(file_path)

    assert actual == expected

def test_raises_error_when_file_does_not_exist(tmp_path):
    missing_file = tmp_path / "missing.py"

    with pytest.raises(FileNotFoundError, match="File not found"):
        read_file(missing_file)

def test_raises_error_when_path_is_directory(tmp_path):
    directory = tmp_path / "sample_folder"
    directory.mkdir()

    with pytest.raises(IsADirectoryError):
        read_file(directory)

def test_rejects_none_as_file_path():
    with pytest.raises(TypeError):
        read_file(None)

def test_rejects_empty_file_path():
    with pytest.raises(ValueError, match="cannot be empty"):
        read_file("")


def test_rejects_invalid_input_type():
    with pytest.raises(TypeError, match="string or Path"):
        read_file(123)


def test_handles_permission_error(tmp_path, monkeypatch):
    file_path = tmp_path / "sample.py"
    file_path.write_text("print('Hello')")

    def mock_open(*args, **kwargs):
        raise PermissionError("Access denied")

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(PermissionError, match="Cannot read file"):
        read_file(file_path)