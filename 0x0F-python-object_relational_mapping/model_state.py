#!/usr/bin/python3
"""
Python file to create class definition of a State and
an instance Base = declarative_base()
"""
# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create instance Base
Base = declarative_base()


# Create a class
class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """__str__ attribute"""
        return "{}".format(self.name)
