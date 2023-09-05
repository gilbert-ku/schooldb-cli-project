from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Create a base class for declarative models
Base = declarative_base()
DATABASE_URI = 'sqlite:///school.db'
engine = create_engine(DATABASE_URI, echo=True)

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, Sequence("student_id_seq"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    address = Column(String)
    contact_information = Column(Integer)


class Teacher(Base):
    __tablename__ = "teachers"
    teacher_id = Column(Integer, Sequence("teacher_id_seq"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    contact_information = Column(Integer)
    subject = Column(String)


class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, Sequence("course_id_seq"), primary_key=True)
    course_name = Column(String)
    course_code = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))


class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"
    enrollment_id = Column(Integer, Sequence("enrollment_id_seq"), primary_key=True)
    enrollment_date = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))


class Grade(Base):
    __tablename__ = "grades"
    grade_id = Column(Integer, Sequence("grade_id_seq"), primary_key=True)
    date_of_grade = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    grade = Column(Integer)
