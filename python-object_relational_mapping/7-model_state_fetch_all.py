#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """Create SQLAlchemy engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    """Create a session to interact with the database"""
    Base.metadata.create_all(engine)
    session = Session(engine)

    """Query the database"""
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
