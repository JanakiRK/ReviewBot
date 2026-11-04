from pathlib import Path


def read_file(file_path: Path) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"File not found: {file_path}"
        ) from error