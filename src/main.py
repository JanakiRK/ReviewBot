
import argparse
import sys

from src.review_engine import review_file


def print_report(result: dict) -> None:
    print("\n========== ReviewBot Report ==========")
    print(f"File: {result['file_path']}")

    if not result["success"]:
        print("\nSYNTAX ERROR:")
        print(result["syntax_error"])
        print("\nReview could not continue.")
        return

    print("\nSyntax: Valid")

    print("\nFunctions:")
    if result["functions"]:
        for function in result["functions"]:
            print(f"  - {function['name']} (line {function['line']})")
    else:
        print("  No functions found.")

    print("\nClasses:")
    if result["classes"]:
        for cls in result["classes"]:
            print(f"  - {cls['name']} (line {cls['line']})")
    else:
        print("  No classes found.")

    print("\nCode Review Issues:")
    if result["issues"]:
        for issue in result["issues"]:
            print(
                f"  - Line {issue['line']}: "
                f"{issue['message']}"
            )
    else:
        print("  No issues found.")

    print("\n======================================")


def main():
    parser = argparse.ArgumentParser(
        description="ReviewBot - Python Code Review Tool"
    )

    parser.add_argument(
        "file",
        help="Path to the Python file you want to review"
    )

    args = parser.parse_args()

    try:
        result = review_file(args.file)
        print_report(result)

        if not result["success"]:
            sys.exit(1)

    except (FileNotFoundError, IsADirectoryError, PermissionError, TypeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
