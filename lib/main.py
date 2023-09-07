# install and import click library
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.exc import IntegrityError

from modules import Student,Teacher, Course, CourseEnrollment

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


def student(first_name, last_name, date_of_birth, address, contact_information):
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
def teacher(first_name, last_name, contact_information, subject):
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
def course(course_name, course_code, teacher_id):
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
def enrollment(student_id, course_id):
    """Enroll a student in a course."""
    enrollment_date = input("Enter the enrollment date (YYYY-MM-DD): ")

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


if __name__ == '__main__':
    add_data()



