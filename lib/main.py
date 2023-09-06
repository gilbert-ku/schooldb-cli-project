#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#define connection

DATABASE_URI = 'sqlite:///school.db'
engine = create_engine (DATABASE_URI, echo=True)

Session = sessionmaker(bind=engine)
session = Session()



session.close()