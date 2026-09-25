-- Day 11: Normalization Practice
-- Starting with a deliberately messy dataset


-- UNNORMALIZED TABLE
CREATE TABLE enrollment_messy (
    student_id INTEGER,
    student_name TEXT,
    student_email TEXT,
    course_id INTEGER,
    course_name TEXT,
    instructor_name TEXT,
    instructor_email TEXT,
    grade TEXT
);


INSERT INTO enrollment_messy VALUES
(1, 'Ali Khan', 'ali@example.com', 101, 'Database Systems', 'Dr. Ahmed', 'ahmed@university.edu', 'A'),
(1, 'Ali Khan', 'ali@example.com', 102, 'Operating Systems', 'Dr. Sara', 'sara@university.edu', 'B+'),
(2, 'Sara Ahmed', 'sara@example.com', 101, 'Database Systems', 'Dr. Ahmed', 'ahmed@university.edu', 'A-'),
(3, 'Hamza Malik', 'hamza@example.com', 103, 'Computer Networks', 'Dr. Ahmed', 'ahmed@university.edu', 'B');


-- 1NF
-- Each field contains a single atomic value.
-- Each row represents one student-course enrollment.


-- 2NF
-- Separate student information, course information,
-- and enrollment information.


CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL
);


CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor_name TEXT NOT NULL,
    instructor_email TEXT NOT NULL
);


CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- Insert normalized data

INSERT INTO students VALUES
(1, 'Ali Khan', 'ali@example.com'),
(2, 'Sara Ahmed', 'sara@example.com'),
(3, 'Hamza Malik', 'hamza@example.com');


INSERT INTO courses VALUES
(101, 'Database Systems', 'Dr. Ahmed', 'ahmed@university.edu'),
(102, 'Operating Systems', 'Dr. Sara', 'sara@university.edu'),
(103, 'Computer Networks', 'Dr. Ahmed', 'ahmed@university.edu');


INSERT INTO enrollments VALUES
(1, 101, 'A'),
(1, 102, 'B+'),
(2, 101, 'A-'),
(3, 103, 'B');


-- 3NF
-- Instructor information can be separated because
-- instructor details depend on the instructor, not directly
-- on the course enrollment.


CREATE TABLE instructors (
    instructor_id INTEGER PRIMARY KEY,
    instructor_name TEXT NOT NULL,
    instructor_email TEXT NOT NULL
);


CREATE TABLE courses_3nf (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor_id INTEGER NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);


INSERT INTO instructors VALUES
(1, 'Dr. Ahmed', 'ahmed@university.edu'),
(2, 'Dr. Sara', 'sara@university.edu');


INSERT INTO courses_3nf VALUES
(101, 'Database Systems', 1),
(102, 'Operating Systems', 2),
(103, 'Computer Networks', 1);