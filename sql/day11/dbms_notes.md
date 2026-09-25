\# Day 11 - DBMS Theory, Normalization \& Indexing



\## 1. Database Normalization



Normalization is the process of organizing data to reduce redundancy and improve data integrity.



\### Unnormalized Table



The starting table was `enrollment\_messy`.



It contained:



\- Student information

\- Course information

\- Instructor information

\- Enrollment/grade information



Example:



| student\_id | student\_name | student\_email | course\_id | course\_name | instructor\_name | instructor\_email | grade |

|---|---|---|---|---|---|---|---|

| 1 | Ali Khan | ali@example.com | 101 | Database Systems | Dr. Ahmed | ahmed@university.edu | A |

| 1 | Ali Khan | ali@example.com | 102 | Operating Systems | Dr. Sara | sara@university.edu | B+ |



This structure contains repeated student and instructor information.



\---



\## 2. First Normal Form (1NF)



A table is in 1NF when:



\- Each column contains atomic values

\- There are no repeating groups

\- Each row represents a single record



The `enrollment\_messy` table already contains atomic values, with each row representing one student-course enrollment.



\---



\## 3. Second Normal Form (2NF)



2NF requires:



\- The table to already be in 1NF

\- No partial dependency on part of a composite key



The data was separated into:



\### Students



\- `student\_id`

\- `student\_name`

\- `student\_email`



\### Courses



\- `course\_id`

\- `course\_name`

\- `instructor\_name`

\- `instructor\_email`



\### Enrollments



\- `student\_id`

\- `course\_id`

\- `grade`



The `enrollments` table uses `(student\_id, course\_id)` as its composite primary key.



\---



\## 4. Third Normal Form (3NF)



3NF requires:



\- The table to already be in 2NF

\- No transitive dependencies



Instructor information was separated from the course table.



\### Instructors



\- `instructor\_id`

\- `instructor\_name`

\- `instructor\_email`



\### Courses



\- `course\_id`

\- `course\_name`

\- `instructor\_id`



This means instructor details are stored only once and courses reference the instructor through `instructor\_id`.



\---



\## 5. Database Indexing



An index is a database structure that helps SQLite find rows more efficiently without scanning the entire table.



For this exercise, the following indexes were created:



```sql

CREATE INDEX idx\_users\_city ON users(city);



CREATE INDEX idx\_orders\_user\_id ON orders(user\_id);



CREATE INDEX idx\_orders\_product\_id ON orders(product\_id);

