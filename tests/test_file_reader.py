from pathlib import Path

from src.file_reader import read_file


def test_reads_file_content(tmp_path):
    file_path = tmp_path / "sample.py"
    expected = "print('Hello ReviewBot')"

    file_path.write_text(expected)

    actual = read_file(file_path)

    assert actual == expected