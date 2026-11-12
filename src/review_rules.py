
import ast


def review_code(source_code: str, max_function_lines: int = 20) -> list:
    tree = ast.parse(source_code)
    issues = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if ast.get_docstring(node) is None:
                issues.append({
                    "rule": "missing_docstring",
                    "message": f"Function '{node.name}' is missing a docstring",
                    "line": node.lineno
                })

            function_lines = node.end_lineno - node.lineno + 1

            if function_lines > max_function_lines:
                issues.append({
                    "rule": "long_function",
                    "message": f"Function '{node.name}' is too long ({function_lines} lines)",
                    "line": node.lineno
                })

        elif isinstance(node, ast.ClassDef):
            if ast.get_docstring(node) is None:
                issues.append({
                    "rule": "missing_docstring",
                    "message": f"Class '{node.name}' is missing a docstring",
                    "line": node.lineno
                })

        elif isinstance(node, ast.ExceptHandler):
            if node.type is None:
                issues.append({
                    "rule": "bare_except",
                    "message": "Bare except statement found",
                    "line": node.lineno
                })

    return issues
