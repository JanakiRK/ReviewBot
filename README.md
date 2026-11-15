## Development and Contribution Guidelines

Anyone working on ReviewBot in the future must follow these rules.

### 1. Project Setup

- Use Python 3.10 or later.
- Clone the repository:
  ```bash
  git clone https://github.com/JanakiRK/ReviewBot.git
  cd ReviewBot
  ```
- Create and activate a virtual environment:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- Install the test dependency:
  ```bash
  python -m pip install pytest
  ```

### 2. Project Structure

Follow the existing project structure. Do not move, rename, or merge modules without a clear technical reason.

- `src/file_reader.py` – Reads and validates Python source files.
- `src/analyser.py` – Performs Python syntax analysis and extracts functions and classes.
- `src/review_rules.py` – Contains code review rules and issue detection.
- `src/review_engine.py` – Coordinates file reading, analysis, and review rules.
- `src/main.py` – Provides the command-line interface.
- `tests/` – Contains automated tests for the project.

Keep responsibilities separate. Do not place all application logic in