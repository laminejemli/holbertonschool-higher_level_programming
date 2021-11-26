#!/usr/bin/python3
"""
Script to change the name of a State object from database hbtn_0e_6_usa
update where id = 2
Arguments taken: mysql username, mysql password, database name
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
    # Start engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    # Create configured class Session
    Session = sessionmaker(bind=engine)
    # Create Session instance
    my_session = Session()
    # Change name of object with 2 as id
    state_to_update = my_session.query(State).filter(State.id == 2).one()
    state_to_update.name = 'New Mexico'
    my_session.commit()
    # Close session
    my_session.close()
