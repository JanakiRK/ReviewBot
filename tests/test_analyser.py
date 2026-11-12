
from src.analyser import analyse_code, extract_definitions


def test_valid_python_code():
    code = "print('Hello World')"

    result = analyse_code(code)

    assert result["success"] is True
    assert result["error"] is None


def test_invalid_python_code():
    code = "def hello("

    result = analyse_code(code)

    assert result["success"] is False
    assert result["error"] is not None

def test_extract_functions():
    code = """
def hello():
    print("Hello")

def goodbye():
    print("Goodbye")
"""

    result = extract_definitions(code)

    assert result["success"] is True
    assert len(result["functions"]) == 2
    assert result["functions"][0]["name"] == "hello"
    assert result["functions"][0]["line"] == 2


def test_extract_classes():
    code = """
class ReviewBot:
    pass
"""

    result = extract_definitions(code)

    assert result["success"] is True
    assert result["classes"][0]["name"] == "ReviewBot"
    assert result["classes"][0]["line"] == 2
