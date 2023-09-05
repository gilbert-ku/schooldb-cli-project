# print("hello wold")
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
    date_of_birth = (Integer)
    address = Column(String)
    Contact_infornation  = Column(Integer)


class Teacher(Base):
    __tablename__ = "teachers"
    teacher_id = Column(Integer, Sequence("teacher_id_sqs"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    Contact_infornation  = Column(Integer)
    subject = Column(String)


class course(Base):
    __tablename__ = "course"
    course_id = Column(Integer, Sequence("course_id_seq"), primary_key=True)
    course_name = Column(String)
    course_code = Column(Integer)
    Teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))


class course_enrollment(Base):
    __tablename__ = "course_enrollment"
    enrollment_id = Column(Integer, Sequence("enrollment_id_seq"), primary_key=True)
    enrollment_date = Column(Integer)
    student_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    course_id = Column(Integer, ForeignKey("course_enrollment.enrollment_id"))



class Grade(Base):
    __tablename__ = "grades"
    date_of_graden= Column(Integer)
    grade_id = Column(Integer, Sequence("grade_id_seq"), primary_key=True)
    student_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    course_id = course_id = Column(Integer, ForeignKey("course_enrollment.enrollment_id"))
    grade = Column = Column(Integer)