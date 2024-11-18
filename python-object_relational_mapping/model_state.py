#!/usr/bin/python3
"""
Defines a State class and an instance of Base for working with SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()

class State(Base):
    """
    State class that maps to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

