# Career Launch

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

