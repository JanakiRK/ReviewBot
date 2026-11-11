

from src.analyser import analyse_code


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
