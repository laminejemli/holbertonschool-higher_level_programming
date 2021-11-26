#!/usr/bin/python3
"""
Script to add the State object 'Louisiana' to database hbtn_0e_6_usa
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
    # Create a Session instance
    my_session = Session()
    # Create a new state
    new_state = State(name='Louisiana')
    # Add new state to my_session
    my_session.add(new_state)
    # Commit the added state
    my_session.commit()
    # Print the id of State added (new_state)
    print("{}".format(new_state.id))
    # Close the session
    my_session.close()
