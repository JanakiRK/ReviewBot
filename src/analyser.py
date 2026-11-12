
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


def extract_definitions(source_code: str) -> dict:
    try:
        tree = ast.parse(source_code)

        functions = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions.append({
                    "name": node.name,
                    "line": node.lineno
                })

            elif isinstance(node, ast.ClassDef):
                classes.append({
                    "name": node.name,
                    "line": node.lineno
                })

        return {
            "success": True,
            "functions": functions,
            "classes": classes,
            "error": None
        }

    except SyntaxError as error:
        return {
            "success": False,
            "functions": [],
            "classes": [],
            "error": str(error)
        }
