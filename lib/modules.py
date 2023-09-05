# print("hello wold")
from sqlalchemy import Column, Integer, String, Sequence
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
    address = (String)
    Contact_infornation  = (Integer)

  