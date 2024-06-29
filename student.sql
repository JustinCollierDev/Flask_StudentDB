CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    amount_due DECIMAL(10, 2)
);