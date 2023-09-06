# install and import click library
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from modules import Student, GradeLookup, grade_lookup_data

# Define the database connection
DATABASE_URI = 'sqlite:///school.db'
engine = create_engine(DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

@click.command()
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

if __name__ == '__main__':
    add_student()
