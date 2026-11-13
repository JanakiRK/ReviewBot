
from pathlib import Path

from src.file_reader import read_file
from src.analyser import analyse_code, extract_definitions
from src.review_rules import review_code


def review_file(file_path: str | Path) -> dict:
    source_code = read_file(file_path)

    syntax_result = analyse_code(source_code)

    if not syntax_result["success"]:
        return {
            "success": False,
            "file_path": str(file_path),
            "syntax_error": syntax_result["error"],
            "functions": [],
            "classes": [],
            "issues": []
        }

    definitions = extract_definitions(source_code)
    issues = review_code(source_code)

    return {
        "success": True,
        "file_path": str(file_path),
        "syntax_error": None,
        "functions": definitions["functions"],
        "classes": definitions["classes"],
        "issues": issues
    }
