#!/usr/bin/python3
"""
Script to delete all State objects with a name containing
the letter 'a' from database hbtn_0e_6_usa
Arguments taken: mysql username, mysql password, database name
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    # Set variables from input
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    # Start engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    # Create configured class Session
    Session = sessionmaker(bind=engine)
    # Create Session instance
    session = Session()
    # Find all objects to delete
    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    # Commit changes
    session.commit()
    # Close session
    session.close()
