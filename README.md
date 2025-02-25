# Python Build & Test System with Bazel

This repository demonstrates how to use Bazel as a build system for Python projects, including automated testing, linting, and formatting.

## Project Structure

```
project-root/
├── src/               # Source code
│   ├── math_utils.py  # Math utility functions
│   ├── string_utils.py# String utility functions
│   ├── BUILD          # Bazel build file for source code
├── tests/             # Unit tests
│   ├── test_math_utils.py
│   ├── test_string_utils.py
│   ├── BUILD          # Bazel build file for tests
├── scripts/           # Helper scripts
│   ├── lint.sh        # Script to run pylint
│   ├── format.sh      # Script to run black formatter
├── requirements.txt   # Python dependencies
├── WORKSPACE          # Bazel workspace configuration
├── BUILD              # Root Bazel build configuration
├── MODULE.bazel       # Bazel module configuration
├── README.md          # This file
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/username/python-bazel-ci.git
   cd python-bazel-ci
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Make scripts executable**:
   ```
   chmod +x scripts/lint.sh
   chmod +x scripts/format.sh
   ```

## Using Bazel Commands

### Run Unit Tests
```sh
# Run all tests
bazel test //tests:all

# Run specific test
bazel test //tests:test_math_utils
bazel test //tests:test_string_utils
```

### Run Linting
```sh
bazel test //:lint
```

### Run Formatting Check
```sh
bazel test //:format
```

## GitHub Actions

This repository is configured with GitHub Actions to automatically run tests, linting, and formatting checks on each push to the main branch and for all pull requests.

## Utility Functions

### Math Utils
- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference between two numbers.
- `multiply(a, b)`: Returns the product of two numbers.
- `divide(a, b)`: Returns the quotient of two numbers.

### String Utils
- `reverse_string(s)`: Returns the reversed string.
- `is_palindrome(s)`: Checks if a string is a palindrome.
- `count_vowels(s)`: Counts the number of vowels in a string.