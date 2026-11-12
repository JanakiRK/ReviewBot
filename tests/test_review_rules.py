
from src.review_rules import review_code


def test_detects_missing_docstring():
    code = """
def hello():
    print("Hello")
"""

    issues = review_code(code)

    assert any(issue["rule"] == "missing_docstring" for issue in issues)


def test_detects_long_function():
    code = """
def hello():
    print("Hello")
    print("World")
    print("Again")
"""

    issues = review_code(code, max_function_lines=2)

    assert any(issue["rule"] == "long_function" for issue in issues)


def test_detects_bare_except():
    code = """
try:
    print("Hello")
except:
    pass
"""

    issues = review_code(code)

    assert any(issue["rule"] == "bare_except" for issue in issues)