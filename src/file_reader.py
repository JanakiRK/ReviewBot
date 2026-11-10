
from pathlib import Path


def read_file(file_path: str | Path) -> str:

    if file_path is None:
        raise TypeError("File path cannot be None")

    if not isinstance(file_path, (str, Path)):
        raise TypeError("File path must be a string or Path")

    if str(file_path) == "":
        raise ValueError("File path cannot be empty")

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

    except PermissionError as error:
        raise PermissionError(
            f"Cannot read file: {file_path}"
        ) from error
