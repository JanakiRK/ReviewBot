
import ast


def analyse_code(source_code: str) -> dict:
    try:
        ast.parse(source_code)

        return {
            "success": True,
            "error": None
        }

    except SyntaxError as error:
        return {
            "success": False,
            "error": str(error)
        }
