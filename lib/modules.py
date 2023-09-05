# print("hello wold")

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# Create a base class for declarative models
Base = declarative_base()
DATABASE_URI = 'sqlite:///school.db'
engine = create_engine(DATABASE_URI, echo=True)

