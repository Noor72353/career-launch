\# Career Launch - Interview Cheat Sheet



A quick reference for Python, Git/GitHub, SQL, pytest, GitHub Actions, and PyInstaller.



\---



\# 1. Python



\## Variables



```python

name = "Ali"

age = 22

is\_student = True

Lists

numbers = \[1, 2, 3, 4, 5]



numbers.append(6)

numbers.remove(3)



first = numbers\[0]

last = numbers\[-1]

Dictionary

user = {

&#x20;   "name": "Ali",

&#x20;   "age": 22,

&#x20;   "city": "Islamabad",

}



print(user\["name"])

List Comprehension

squares = \[x \* x for x in range(10)]



With condition:



even\_numbers = \[x for x in numbers if x % 2 == 0]

Functions

def add(a, b):

&#x20;   return a + b



Default argument:



def greet(name="User"):

&#x20;   return f"Hello, {name}"

\*args and \*\*kwargs

def add\_all(\*args):

&#x20;   return sum(args)

def show\_user(\*\*kwargs):

&#x20;   print(kwargs)

Lambda

square = lambda x: x \* x

Map / Filter

squares = list(map(lambda x: x \* x, numbers))



even = list(filter(lambda x: x % 2 == 0, numbers))

Exception Handling

try:

&#x20;   result = 10 / 0

except ZeroDivisionError:

&#x20;   print("Cannot divide by zero")

finally:

&#x20;   print("Finished")

File Handling

with open("data.txt", "r") as file:

&#x20;   data = file.read()



Write:



with open("data.txt", "w") as file:

&#x20;   file.write("Hello")

Classes

class User:

&#x20;   def \_\_init\_\_(self, name):

&#x20;       self.name = name



&#x20;   def greet(self):

&#x20;       return f"Hello {self.name}"

Inheritance

class Student(User):

&#x20;   pass

Generator



Generators use yield and produce values one at a time.



def numbers():

&#x20;   for i in range(5):

&#x20;       yield i

Decorator

def timer(func):

&#x20;   def wrapper(\*args, \*\*kwargs):

&#x20;       print("Running function")

&#x20;       return func(\*args, \*\*kwargs)



&#x20;   return wrapper



Usage:



@timer

def hello():

&#x20;   print("Hello")

Context Manager

with open("data.txt") as file:

&#x20;   data = file.read()



Custom context managers use:



\_\_enter\_\_()

\_\_exit\_\_()

2\. Python Interview Patterns

Two Sum

def two\_sum(nums, target):

&#x20;   seen = {}



&#x20;   for i, num in enumerate(nums):

&#x20;       complement = target - num



&#x20;       if complement in seen:

&#x20;           return \[seen\[complement], i]



&#x20;       seen\[num] = i



&#x20;   return \[]



Time: O(n)



Space: O(n)



Frequency Counter

from collections import Counter



counts = Counter(nums)

Stack

stack = \[]



stack.append(10)

stack.append(20)



value = stack.pop()

Queue

from collections import deque



queue = deque()



queue.append(10)

queue.append(20)



value = queue.popleft()

Sorting

numbers.sort()



Without modifying original:



sorted\_numbers = sorted(numbers)

3\. Git and GitHub

Check Status

git status

Initialize Repository

git init

Add Files

git add .



Specific file:



git add README.md

Commit

git commit -m "Add feature"

Push

git push origin main

Pull

git pull origin main

Clone

git clone <repository-url>

View Remote

git remote -v

View Commit History

git log --oneline



Latest commit:



git log -1 --oneline

Create Branch

git checkout -b feature-name



Modern command:



git switch -c feature-name

Switch Branch

git switch main

Merge

git merge feature-name

Undo Unstaged Changes

git restore filename

Unstage File

git restore --staged filename

Git Diff

git diff



Staged changes:



git diff --cached

4\. SQL Basics

SELECT

SELECT \*

FROM users;



Specific columns:



SELECT name, email

FROM users;

WHERE

SELECT \*

FROM users

WHERE city = 'Islamabad';

ORDER BY

SELECT \*

FROM users

ORDER BY name ASC;



Descending:



SELECT \*

FROM users

ORDER BY name DESC;

LIMIT

SELECT \*

FROM users

LIMIT 5;

INSERT

INSERT INTO users (name, email, city)

VALUES ('Ali', 'ali@example.com', 'Islamabad');

UPDATE

UPDATE users

SET city = 'Lahore'

WHERE id = 1;

DELETE

DELETE FROM users

WHERE id = 1;



Always use WHERE carefully.



5\. SQL JOINs

INNER JOIN



Returns matching rows from both tables.



SELECT students.name, courses.name

FROM students

INNER JOIN enrollments

&#x20;   ON students.id = enrollments.student\_id

INNER JOIN courses

&#x20;   ON courses.id = enrollments.course\_id;

LEFT JOIN



Returns all rows from the left table and matching rows from the right table.



SELECT users.name, orders.id

FROM users

LEFT JOIN orders

&#x20;   ON users.id = orders.user\_id;

Multiple Tables

SELECT

&#x20;   students.name,

&#x20;   courses.name,

&#x20;   instructors.name

FROM students

JOIN enrollments

&#x20;   ON students.id = enrollments.student\_id

JOIN courses

&#x20;   ON courses.id = enrollments.course\_id

JOIN instructors

&#x20;   ON courses.instructor\_id = instructors.id;

6\. SQL Aggregation

COUNT

SELECT COUNT(\*)

FROM users;

GROUP BY

SELECT city, COUNT(\*)

FROM users

GROUP BY city;

HAVING

SELECT city, COUNT(\*)

FROM users

GROUP BY city

HAVING COUNT(\*) > 1;



Important:



WHERE filters rows before grouping.

HAVING filters groups after grouping.

SUM / AVG / MIN / MAX

SELECT

&#x20;   SUM(amount),

&#x20;   AVG(amount),

&#x20;   MIN(amount),

&#x20;   MAX(amount)

FROM orders;

7\. SQL Subqueries

Example

SELECT name

FROM employees

WHERE salary > (

&#x20;   SELECT AVG(salary)

&#x20;   FROM employees

);



A subquery is a query inside another query.



8\. SQL Normalization

1NF

Atomic values

No repeating groups

Each column contains one value

2NF

Must be in 1NF

No partial dependency on part of a composite key

3NF

Must be in 2NF

No transitive dependency

Non-key columns should depend on the key



Example normalized structure:



Students

\--------

student\_id

name

email



Courses

\-------

course\_id

course\_name

instructor\_id



Instructors

\-----------

instructor\_id

name

email



Enrollments

\-----------

student\_id

course\_id

9\. SQL Indexing



Create index:



CREATE INDEX idx\_users\_city

ON users(city);



Check indexes in SQLite:



sqlite3 practice.db ".indexes"



Query plan:



EXPLAIN QUERY PLAN

SELECT \*

FROM users

WHERE city = 'Islamabad';



Without index:



SCAN users



With index:



SEARCH users USING INDEX idx\_users\_city



Indexes can improve lookup performance but also require storage and can add overhead to inserts and updates.



10\. SQLite



Open database:



sqlite3 practice.db



List tables:



.tables



Show schema:



.schema



Exit:



.quit



Run SQL file:



Get-Content normalization.sql | sqlite3 practice.db



Query from PowerShell:



sqlite3 practice.db "SELECT \* FROM users;"

11\. Pandas



Import:



import pandas as pd



Create DataFrame:



df = pd.DataFrame({

&#x20;   "name": \["Ali", "Sara"],

&#x20;   "city": \["Islamabad", "Rawalpindi"],

})



Read CSV:



df = pd.read\_csv("data.csv")



View first rows:



df.head()



Select column:



df\["name"]



Filter:



df\[df\["city"] == "Islamabad"]



Basic information:



df.info()



Statistics:



df.describe()

12\. pytest



Install:



pip install pytest



Run all tests:



pytest



Run a specific file:



pytest test\_file.py



Run with verbose output:



pytest -v



Example test:



def add(a, b):

&#x20;   return a + b





def test\_add():

&#x20;   assert add(2, 3) == 5



Useful assertions:



assert result == expected

assert value is not None

assert item in collection

13\. Flake8



Install:



pip install flake8



Run on project directories:



flake8 dsa cv sql



Create configuration:



.flake8



Purpose:



Detect syntax and style problems

Find unused imports

Detect undefined names

Enforce code quality rules

14\. GitHub Actions



Workflow location:



.github/workflows/python-ci.yml



Basic workflow structure:



name: Python CI



on:

&#x20; push:

&#x20;   branches:

&#x20;     - main

&#x20; pull\_request:

&#x20;   branches:

&#x20;     - main



jobs:

&#x20; test:

&#x20;   runs-on: ubuntu-latest



&#x20;   steps:

&#x20;     - uses: actions/checkout@v4



&#x20;     - uses: actions/setup-python@v5

&#x20;       with:

&#x20;         python-version: "3.13"



&#x20;     - run: pip install pytest flake8



&#x20;     - run: pytest



&#x20;     - run: flake8 dsa cv sql



Purpose:



Automatically run tests

Automatically check code quality

Detect problems before merging

Provide a green or red CI status

15\. Virtual Environment



Create:



py -3.13 -m venv .venv



Activate on Windows PowerShell:



.\\.venv\\Scripts\\Activate.ps1



Install package:



pip install package-name



Check installed packages:



pip list



Deactivate:



deactivate

16\. PyInstaller



Install:



pip install pyinstaller



Basic build:



pyinstaller app.py



Single executable:



pyinstaller --onefile app.py



GUI application without console:



pyinstaller --onefile --windowed app.py



Add icon:



pyinstaller --onefile --windowed --icon=app.ico app.py



Clean previous build:



pyinstaller --clean --onefile app.py



Output:



dist/

build/

app.spec



The executable is normally created inside:



dist/

17\. Useful Python Commands



Check Python version:



python --version



Check Python launcher:



py --version



Find Python:



where.exe python



Upgrade pip:



python -m pip install --upgrade pip



Install from requirements:



pip install -r requirements.txt



Generate requirements:



pip freeze > requirements.txt

18\. Interview Quick Answers

What is a list?



An ordered, mutable collection of values.



What is a tuple?



An ordered, immutable collection of values.



What is a dictionary?



A mutable collection of key-value pairs.



List vs tuple?



Lists are mutable; tuples are immutable.



What is a generator?



A function that produces values lazily using yield.



What is a decorator?



A function that modifies or extends the behavior of another function.



What is a context manager?



An object that manages setup and cleanup, commonly used with with.



What is normalization?



Organizing database tables to reduce redundancy and improve data integrity.



What is an index?



A database structure that can speed up data retrieval.



INNER JOIN vs LEFT JOIN?



INNER JOIN returns matching rows from both tables.



LEFT JOIN returns all rows from the left table and matching rows from the right table.



WHERE vs HAVING?



WHERE filters rows.



HAVING filters grouped results.



What is CI?



Continuous Integration automatically builds, tests, and checks code whenever changes are pushed.



What is pytest?



A Python testing framework used to write and run automated tests.



What is PyInstaller?



A tool that packages Python applications into standalone executables.



19\. Daily Git Workflow

git status

git add .

git commit -m "Describe changes"

git push origin main

git status



Expected final state:



Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

20\. Interview Reminder



When explaining a project:



Explain the problem.

Explain the solution.

Explain the technologies used.

Explain your specific contribution.

Mention an important technical challenge.

Explain how you solved it.

Mention testing and validation.

Explain what you learned.



Day 13 - Cheat Sheet Completed ✅

