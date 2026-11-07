from pathlib import Path


def read_file(file_path: Path) -> str:
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.is_file():
        raise IsADirectoryError(f"Not a file: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"File not found: {file_path}"
        ) from error