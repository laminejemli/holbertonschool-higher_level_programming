#!/usr/bin/python3
"""
Script that prints the id of State objects from database
hbtn_0e_6_usa with name passed as an argument.
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    # Set variables to input arguments
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    # Start enginge
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    # Create configured class Session
    Session = sessionmaker(bind=engine)
    # Create a Session instance
    my_session = Session()
    # my_session work
    object = my_session.query(State).filter(
        State.name == state_name).first()
    if object:
        print("{}".format(object.id))
    else:
        print("Not found")
    # Close session
    my_session.close()
