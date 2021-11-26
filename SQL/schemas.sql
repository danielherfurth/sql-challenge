-- drop table if it exists and break dependencies
DROP TABLE IF EXISTS titles CASCADE;
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS dept_emp CASCADE;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS dept_mgr CASCADE;

CREATE TABLE titles (
                        title_id CHAR(5) PRIMARY KEY,
                        title VARCHAR NOT NULL
                    );


CREATE TABLE departments (
                             dept_no CHAR(4) PRIMARY KEY,
                             dept_name VARCHAR NOT NULL
                         );


CREATE TABLE employees (
                           emp_no INT NOT NULL PRIMARY KEY,
                           title_id CHAR(5) REFERENCES titles (title_id),
                           birthdate VARCHAR NOT NULL,
                           first_name VARCHAR NOT NULL,
                           last_name VARCHAR NOT NULL,
                           sex CHAR(1) NOT NULL,
                           hire_date VARCHAR NOT NULL
                       );


-- many-to-many tables require the 2 columns to both be used for primary key
CREATE TABLE dept_emp (
                          emp_no INT REFERENCES employees (emp_no),
                          dept_no CHAR(4) NOT NULL REFERENCES departments (dept_no),
                          PRIMARY KEY (emp_no, dept_no)
                      );


CREATE TABLE salaries (
                          emp_no INT PRIMARY KEY REFERENCES employees (emp_no),
                          salary INT NOT NULL
                      );



CREATE TABLE dept_mgr (
                          dept_no CHAR(4) NOT NULL REFERENCES departments (dept_no),
                          emp_no INT REFERENCES employees (emp_no),
                          PRIMARY KEY (dept_no, emp_no)
                      );

