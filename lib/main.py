# install and import click library
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from modules import Student,Teacher, Course, CourseEnrollment, Grade

# Define the database connection
DATABASE_URI = 'sqlite:///school.db'
engine = create_engine(DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# allow us to have option when we want to a
@click.group()
def add_data():
    pass

# add students
@add_data.command()
@click.option('--first-name', prompt='Enter first name', required=True)
@click.option('--last-name', prompt='Enter last name', required=True)
@click.option('--date-of-birth', prompt='Enter date of birth (YYYY-MM-DD)', required=True)
@click.option('--address', prompt='Enter address', required=True)
@click.option('--contact-information', prompt='Enter contact information', required=True)


def add_student(first_name, last_name, date_of_birth, address, contact_information):
    try:
        # Convert date_of_birth to a Python date object
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()

        # Create a new student object
        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            address=address,
            contact_information=contact_information,
        )

        # Add the student to the database
        session.add(new_student)

        # Commit the changes
        session.commit()
        print("Student added successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        session.rollback()

# add teacher
@add_data.command()
@click.option('--first-name', prompt='Enter first name', required=True)
@click.option('--last-name', prompt='Enter last name', required=True)
@click.option('--contact-information', prompt='Enter contact information', required=True)
@click.option('--subject', prompt='Enter subject', required=True)
def add_teacher(first_name, last_name, contact_information, subject):
    try:
        # Create a new teacher object
        new_teacher = Teacher(
            first_name=first_name,
            last_name=last_name,
            contact_information=contact_information,
            subject=subject
        )

        # Add the teacher to the session
        session.add(new_teacher)

        # Commit the changes to insert the teacher into the database
        session.commit()
        print("Teacher added successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        session.rollback()

#add courses and teacher
@add_data.command()
@click.option('--course-name', prompt='Enter course name', required=True)
@click.option('--course-code', prompt='Enter course code', required=True, type=int)
@click.option('--teacher-id', prompt='Enter teacher ID', required=True, type=int)
def add_course(course_name, course_code, teacher_id):
    try:
        # Check if the teacher with the provided teacher_id exists in the database
        teacher = session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        
        if teacher is None:
            raise IntegrityError(None, None, "Teacher ID does not exist in the database.")
        
        # Create a new course object
        course = Course(
            course_name=course_name,
            course_code=course_code,
            teacher_id=teacher_id
        )

        # Add the course to the database
        session.add(course)

        # Commit the changes
        session.commit()
        print("Course added successfully!")

    except IntegrityError as e:
        print(f"Error: {str(e)}")
        session.rollback()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        session.rollback()
    finally:
        session.close()

# enroll student course

@add_data.command()
@click.option("--student-id", type=int, prompt=True, help="Enter the student ID")
@click.option("--course-id", type=int, prompt=True, help="Enter the course ID")
def enroll_student(student_id, course_id):
    """Enroll a student in a course."""
    enrollment_date = input("Enter the enrollment date (YYYY-MM-DD): ")
    enrollment_date = datetime.strptime(enrollment_date, '%Y-%m-%d').date()

    try:
        # Create a new CourseEnrollment object
        new_enrollment = CourseEnrollment(
            enrollment_date=enrollment_date,
            student_id=student_id,
            course_id=course_id
        )

        # Create a session and add the new enrollment to it
        session = Session()
        session.add(new_enrollment)
        session.commit()
        session.close()

        click.echo(f"Student with ID {student_id} enrolled in course with ID {course_id}.")
    except Exception as e:
        click.echo(f"Error: Unable to enroll student in the course. {str(e)}")



# recode grade
@add_data.command()
@click.option('--student-id', prompt='Student ID', type=int, help='Enter the student ID')
@click.option('--course-id', prompt='Course ID', type=int, help='Enter the course ID')
@click.option('--grade-value', prompt='Grade (0-100)', type=int, help='Enter the grade (0-100)')
def record_grade(student_id, course_id, grade_value):
    """Record a grade for a student in a course."""
    engine = create_engine('sqlite:///school.db')  # Use your database URL or connection settings
    Session = sessionmaker(bind=engine)
    session = Session()

    # Check if the student and course exist
    if not session.query(Grade).filter_by(student_id=student_id, course_id=course_id).first():
        print("Error: No existing grade found for this student in this course.")
        session.close()
        return

    # Create a new Grade instance and record the grade
    grade = Grade(student_id=student_id, course_id=course_id, grade_value=grade_value)
    session.add(grade)
    session.commit()

    print("Grade recorded successfully.")

# Define a new command to query all student records
@add_data.command()
def query_students():
    try:
        # Query all student records
        all_students = session.query(Student).all()

        for student in all_students:
            print(f"Student ID: {student.student_id}")
            print(f"First Name: {student.first_name}")
            print(f"Last Name: {student.last_name}")
            print(f"Date of Birth: {student.date_of_birth}")
            print(f"Address: {student.address}")
            print(f"Contact Information: {student.contact_information}")
            print("\n")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Define a new command to query all teacher records
@add_data.command()
def query_teachers():
    try:
        all_teachers = session.query(Teacher).all()

        for teacher in all_teachers:
            print(f"Teacher ID: {teacher.teacher_id}")
            print(f"First Name: {teacher.first_name}")
            print(f"Last Name: {teacher.last_name}")
            print(f"Contact Information: {teacher.contact_information}")
            print(f"Subject: {teacher.subject}")
            print("\n")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def menu():
    while True:
        print("""
    Welcome to the School Management CLI App!

    This app allows you to manage students, teachers, courses, enrollments, and grades in a school database. You can perform various operations such as adding students and teachers, enrolling students in courses, recording grades, and querying student and teacher records.

    To get started, simply choose an option from the menu below or type '8' to exit the app:

    1. Add Student
    2. Add Teacher
    3. Add Course
    4. Enroll Student in Course
    5. Record Grade
    6. Query Students
    7. Query Teachers
    8. Exit

    Feel free to explore the functionalities of this app. If you have any questions or need assistance, type '8' to exit, and we'll be happy to help!
    """)
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Record Grade")
        print("6. Query Students")
        print("7. Query Teachers")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Student
            add_student()
        elif choice == '2':
            # Add Teacher
            add_teacher()
        elif choice == '3':
            # Add Course
            add_course()
        elif choice == '4':
            # Enroll Student in Course
            enroll_student()
        elif choice == '5':
            # Record Grade
            record_grade()
        elif choice == '6':
            # Query Students
            query_students()
        elif choice == '7':
            # Query Teachers
            query_teachers()
        elif choice == '8':
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()

# if __name__ == '__main__':
#     add_data()