#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """Connect to the database"""
    connection_str = (
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3])
    )

    """Create an SQLAlchemy engine"""
    engine = create_engine(connection_str)

    Base.metadata.create_all(engine)
    """Create a session for interacting with the database"""
    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')
