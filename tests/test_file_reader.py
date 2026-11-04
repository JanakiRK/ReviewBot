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