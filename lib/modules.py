from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Date, CheckConstraint, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship

# Create a base class for declarative models
Base = declarative_base()
DATABASE_URI = 'sqlite:///school.db'  # Update with your preferred database URI
engine = create_engine(DATABASE_URI, echo=True)  # Set echo to False in production

class Student(Base):
    __tablename__ = "students"
    # Add a unique constraint for contact information
    __table_args__ = (
        UniqueConstraint("contact_information", name="unique_contact_information"),
    )
    student_id = Column(Integer, Sequence("student_id_seq"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)  
    address = Column(String)
    contact_information = Column(String)  # Changed to String for contact info

    # Define the relationship with CourseEnrollment and Grade
    enrollments = relationship("CourseEnrollment", back_populates="student")
    grades = relationship("Grade", back_populates="student")

class Teacher(Base):
    __tablename__ = "teachers"
    # Add a unique constraint for contact information
    __table_args__ = (
        UniqueConstraint("contact_information", name="unique_contact_information"),
    )
    teacher_id = Column(Integer, Sequence("teacher_id_seq"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    contact_information = Column(String)
    subject = Column(String)

    # Define the relationship with Course
    courses = relationship("Course", back_populates="teacher")

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, Sequence("course_id_seq"), primary_key=True)
    course_name = Column(String)
    course_code = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))

    # Define the relationship with CourseEnrollment and Grade
    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("CourseEnrollment", back_populates="course")
    grades = relationship("Grade", back_populates="course")

class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"
    enrollment_id = Column(Integer, Sequence("enrollment_id_seq"), primary_key=True)
    enrollment_date = Column(Date)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    # Define the relationships with Student and Course
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Grade(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, Sequence("grade_id_seq"), primary_key=True)
    date_of_grade = Column(Date)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    
    # Store the grade as an integer (0-100)
    grade_value = Column(Integer)
    
    # Define the relationships with Student and Course
    student = relationship("Student", back_populates="grades")
    course = relationship("Course", back_populates="grades")


# Create the tables in the database
Base.metadata.create_all(engine)
