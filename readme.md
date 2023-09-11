

# School database.

---
### By: Gilbert Kutoto (Software Engineer)
#### 1. Slack/Mattermost - Gilbert.
#### 2. linkedin - Gilbert Kutoto
#### 3. Email - gilbert45ku@gmail.com
---

## Design pattern:

* https://dbdiagram.io/d/64f3962002bd1c4a5edb9467

## Table of Content:

1. Description.
2. Project Setup.
4. Installation Requirements.
5. Technology Used.
6. How to run & test this app.
7. License.

# School Management CLI App

Welcome to the School Management CLI App! This command-line application allows you to manage student and teacher records, courses, enrollments, and grades in a school database.

## Features

- Add Student: Add new student records with personal information.
- Add Teacher: Add teacher profiles with personal information and subjects.
- Add Course: Create new courses and assign teachers.
- Enroll Student in Course: Enroll students in specific courses.
- Record Grade: Record student grades for courses.
- Query Students: Retrieve and display student records.
- Query Teachers: Retrieve and display teacher records.

---
## Project Setup:

### Installation Requirements:
1. A Functional Laptop.
2. A good internet connection.
3. VS Code.

---

### Technology Used:

#### Ubuntu:
A widely used open-source operating system based on Linux, known for its user-friendly interface and community-driven development.

#### VS CODE:
A source code editor that offers a wide range of features for developers, including debugging, extensions, and customization options.

#### Github:
A web-based platform where developers can store, manage, and share their code repositories and collaborate on projects among developers worldwide.

#### Python:
A high-level, interpreted programming language known for its simplicity, readability, and versatility. It emphasizes clean code and supports multiple programming paradigms, including object-oriented and functional programming.

#### SQLAlchemy:
SQLAlchemy is a Python library for working with relational databases, providing a high-level API to interact with database systems.

#### Alembic:
Alembic is a database migration tool for SQLAlchemy that automates the creation, management, and application of database schema changes, ensuring database schemas evolve with code changes in a controlled manner.

#### CLI:
A Command Line Interface (CLI) is a text-based user interface where users interact with a computer or software by typing commands and receiving text-based responses.

---

### How to Run this Application:
Need a Terminal (Mac or Linux) or Command Prompt(Windows)

To run this project, please follow the following instructions.
* Get access to the internet.
* Clone the repository.

      $ git clone `https://github.com/gilbert-ku/schooldb-cli-project.git`
      $ cd schooldb-cli-project

### How to Test this Application:
1. Install the required dependencies (if any).
pipeny install
pipenv shell
pipenv install sqlachemy
pip install click
2. Run the application using `python main.py`


### How to use the app

This app allows you to manage students, teachers, courses, enrollments, and grades in a school database. You can perform various operations such as adding students and teachers, enrolling students in courses, recording grades, and querying student and teacher records.

To get started, simply choose an option from the menu below or type '8' to exit the app:

1. Add Student
2. Add Teacher
3. Add Course
4. Enroll Student in Course
5. Record Grade
6. List of Students
7. List of Teachers
8. Exit

### Bugs:

None at the moment, but would love to hear your feedback!

---

## License
MIT License

Copyright (c) [2023] [Gilbert Owino]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---
