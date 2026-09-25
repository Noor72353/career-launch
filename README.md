# Career Launch

[![Python](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-pytest-green)](https://pytest.org/)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-black)](https://black.readthedocs.io/)
[![Linting](https://img.shields.io/badge/Linting-Flake8-blue)](https://flake8.pycqa.org/)
[![Coverage](https://img.shields.io/badge/Coverage-85%25-green)](https://pytest-cov.readthedocs.io/)

A structured learning and practice repository for building strong foundations in Python, Data Structures & Algorithms, Computer Vision, SQL, Git, and software development.

## Week 1 - Day 1

### Python Environments

Created three separate Python virtual environments:

* `dsa` - Data Structures & Algorithms practice
* `cv` - Computer Vision practice
* `sql` - SQL learning and practice

Each environment uses Python 3.13.

### Development Tools

Installed and tested:

* pytest - testing
* black - code formatting
* flake8 - code linting

### Project Structure

```text
career-launch/
├── dsa/
│   ├── hello.py
│   ├── test_hello.py
│   ├── two_sum.py
│   └── stock.py
├── cv/
│   ├── hello.py
│   └── test_hello.py
├── sql/
│   ├── hello.py
│   └── test_hello.py
├── .gitignore
└── README.md
```

> Each folder has its own local `.venv` virtual environment, which is excluded from Git using `.gitignore`.

### DSA Practice

Two foundational DSA problems were implemented and tested:

#### 1. Two Sum

* Uses a hash map/dictionary
* Time complexity: O(n)
* Space complexity: O(n)

#### 2. Best Time to Buy and Sell Stock

* Uses a single-pass approach
* Tracks the minimum price seen so far
* Time complexity: O(n)
* Space complexity: O(1)

### Testing

All practice environments were tested using pytest.

Current tests:

* DSA: 1 passed
* CV: 1 passed
* SQL: 1 passed

The DSA solutions were also tested with multiple example inputs.

## Goals

* Strengthen Python fundamentals
* Practice Data Structures & Algorithms
* Learn Computer Vision concepts
* Build SQL skills
* Improve Git and GitHub workflow
* Build a consistent software development practice
* Develop practical problem-solving skills

## Progress

* [x] Python virtual environments
* [x] pytest setup
* [x] Black setup
* [x] Flake8 setup
* [x] Git repository
* [x] First Git commit
* [x] GitHub repository
* [x] First GitHub push
* [x] README documentation
* [x] Two Sum
* [x] Best Time to Buy and Sell Stock


## **Day 1 - Completed ✅**

---

## **Day 2 - OOP Practice**

### OOP Notes

* Inheritance represents an **IS-A** relationship where a child class reuses or extends a parent class.
* Composition represents a **HAS-A** relationship where one class contains or uses objects of another class.
* Use inheritance for specialized versions of a class, while composition is useful when a class needs to use other objects as components.

### Project Structure

```text
career-launch/
├── dsa/
│   ├── hello.py
│   ├── test_hello.py
│   ├── two_sum.py
│   ├── stock.py
│   ├── oop_basics.py
│   ├── test_oop_basics.py
│   ├── contains_duplicate.py
│   └── valid_anagram.py
├── cv/
├── sql/
├── .gitignore
└── README.md
```

## **Day 2 - Completed ✅**

---

## **Day 3 - Advanced Python & DSA**

### Advanced Python

- Decorators
- Generators
- Context Managers
- Added docstrings to the examples
- Used Black for code formatting
- Used Flake8 for code quality checking

### DSA Practice

#### 1. Group Anagrams

- Groups words that are anagrams of each other
- Uses sorted words as grouping keys
- Uses a dictionary to store anagram groups

#### 2. Top K Frequent Elements

- Uses `Counter` to count element frequencies
- Uses `most_common(k)` to find the most frequent elements

### Files Created

- `advanced_python.py`
- `group_anagrams.py`
- `top_k_frequent.py`

## **Day 3 - Completed ✅**

---

## **Day 4 - Git, GitHub Workflow & DSA**

### Git & GitHub Workflow

- Created and worked on the `feature/utils` branch
- Added reusable utility functions in `dsa/utils.py`
- Added pytest tests in `dsa/test_utils.py`
- Updated `.gitignore` using a Python-focused template
- Committed changes with a clear Git commit message
- Pushed the feature branch to GitHub
- Created and self-reviewed a Pull Request
- Merged the Pull Request into `main`
- Deleted the local and remote feature branch after merging

### DSA Practice

#### 1. Product of Array Except Self

- Uses prefix and suffix products
- Does not use division
- Time complexity: O(n)
- Handles arrays containing zero

#### 2. Longest Consecutive Sequence

- Uses a set for fast lookups
- Starts counting only from the beginning of a sequence
- Time complexity: O(n)
- Handles duplicate values

### Testing & Code Quality

- Added pytest tests for both DSA problems
- All tests passed
- Used Black for code formatting
- Used Flake8 for code quality checking

### Documentation

- Added `CONTRIBUTING.md`
- Updated project documentation
- Added project badges

### Day 4 Files

- `dsa/utils.py`
- `dsa/test_utils.py`
- `dsa/product_of_array_except_self.py`
- `dsa/test_product_of_array_except_self.py`
- `dsa/longest_consecutive.py`
- `dsa/test_longest_consecutive.py`
- `.gitignore`
- `CONTRIBUTING.md`

## **Day 4 - Completed ✅**

---

## **Day 5 - Testing with pytest**

### Testing with pytest

- Expanded unit tests for `BankAccount`, `SavingsAccount`, and `CurrentAccount`
- Added tests for utility functions in `utils.py`
- Covered happy paths and edge cases
- Tested invalid inputs and printed error messages using `capsys`
- Added tests for existing DSA solutions
- Added tests for 3Sum and Container With Most Water

### DSA Practice

#### 1. 3Sum

- Finds unique triplets that sum to zero
- Uses sorting and the two-pointer technique
- Handles duplicate values
- Time complexity: O(n²)

#### 2. Container With Most Water

- Finds the maximum amount of water a container can hold
- Uses the two-pointer technique
- Time complexity: O(n)
- Uses constant extra space

### Test Coverage

- Full test suite: **51/51 tests passed**
- Overall test coverage: **85%**
- Coverage target: **80%+**
- Used `pytest-cov` to measure coverage

### Code Quality

- Ran Black successfully
- Ran Flake8 successfully
- Excluded `.venv` from Flake8 because it contains third-party packages

### Day 5 Files

- `dsa/test_oop_basics.py`
- `dsa/test_utils.py`
- `dsa/test_two_sum.py`
- `dsa/test_contains_duplicate.py`
- `dsa/test_valid_anagram.py`
- `dsa/test_group_anagrams.py`
- `dsa/test_top_k_frequent.py`
- `dsa/three_sum.py`
- `dsa/test_three_sum.py`
- `dsa/container_with_most_water.py`
- `dsa/test_container_with_most_water.py`

## **Day 5 - Completed ✅**

---

## **Day 6 - Packaging + PyInstaller**

### Packaging & CLI Tool

* Converted `utils.py` into a command-line interface (CLI) tool using Python's `argparse`
* Added three CLI operations:

  * `even` — checks whether a number is even
  * `square` — calculates the square of a number
  * `reverse` — reverses a string
* Added `pyproject.toml` for Python project packaging
* Configured `setuptools` to package only the `utils.py` module
* Added the `career-utils` command-line entry point
* Installed the project in editable mode
* Tested the CLI successfully using `career-utils`

### CLI Examples

```powershell
career-utils even 10
career-utils square 7
career-utils reverse hello
```

Example output:

```text
True
49
olleh
```

### PyInstaller

* Installed PyInstaller 6.22.3
* Built a standalone Windows executable using PyInstaller
* Used the `--onefile` option to create a single executable
* Successfully generated `utils.exe`
* Tested the standalone executable successfully

### Build Command

From the `dsa` directory:

```powershell
pyinstaller --onefile utils.py
```

The executable is generated in:

```text
dsa/dist/utils.exe
```

### Running the Standalone Executable

```powershell
.\dist\utils.exe even 10
.\dist\utils.exe square 7
.\dist\utils.exe reverse hello
```

Example output:

```text
True
49
olleh
```

### Git Configuration

Added PyInstaller-generated files and directories to `.gitignore`:

```gitignore
# PyInstaller
build/
dist/
*.spec
```

This prevents generated build files from being committed to the repository.

### DSA Practice

#### Longest Substring Without Repeating Characters

* Implemented `length_of_longest_substring()`
* Used the sliding-window technique
* Used a set to track characters currently in the window
* Handles repeated characters
* Handles empty strings
* Time complexity: O(n)
* Space complexity: O(n)

### Testing

* Added 5 tests for Longest Substring Without Repeating Characters
* Full test suite: **56/56 tests passed**
* Overall test coverage: **83%**
* Coverage target: **80%+**
* Used `pytest-cov` to measure coverage

### Code Quality

* Ran Black successfully
* Ran Flake8 successfully
* Excluded `.venv` from Flake8 because it contains third-party packages
* Fixed the line-length issue in `longest_substring.py`

### Day 6 Files

* `dsa/utils.py`
* `dsa/pyproject.toml`
* `dsa/longest_substring.py`
* `dsa/test_longest_substring.py`
* `dsa/.gitignore`

## **Day 6 - Completed ✅**

---

# 🗓️ WEEK 2 — SQL, DBMS + CI + Consolidation

## **Day 8 - SQL Fundamentals**

### SQL Fundamentals

- Completed SQLBolt Lessons 1–6
- Practiced `SELECT`, `WHERE`, `LIKE`, `ORDER BY`, `LIMIT`, `BETWEEN`, and `OR`
- Reviewed basic SQL filtering and sorting

### SQLite Database

- Created a SQLite database named `practice.db`
- Created three tables:
  - `users`
  - `products`
  - `orders`
- Added primary keys and foreign key relationships
- Added sample data using `seed.sql`

### SQL Queries

- Created `queries.sql` containing 15 documented SQL queries
- Practiced:
  - `SELECT`
  - `WHERE`
  - `LIKE`
  - `BETWEEN`
  - `ORDER BY ASC`
  - `ORDER BY DESC`
  - `LIMIT`
  - `OR`

### Database Verification

- Verified all three tables successfully
- `users`: 6 records
- `products`: 7 records
- `orders`: 10 records
- Successfully executed all 15 queries

### LeetCode SQL Practice

Completed:

- Problem 595 — Big Countries
- Problem 584 — Find Customer Referee
- Problem 183 — Customers Who Never Order

### Day 8 Files

- `sql/day8/practice.db`
- `sql/day8/schema.sql`
- `sql/day8/seed.sql`
- `sql/day8/queries.sql`

## **Day 8 - Completed ✅**

---


