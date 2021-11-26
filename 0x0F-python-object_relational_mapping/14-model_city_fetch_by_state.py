#!/usr/bin/python3
"""
Script to print all City objects from database hbtn_0e_14_usa
Arguments taken: mysql username, mysql password, database name
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    from model_city import City
    # Set variables as input
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    # Create a configured class Session
    Session = sessionmaker(bind=engine)
    # Create an instance of Session
    my_session = Session()
    # Find all City objects
    cities = my_session.query(City).join(State).order_by(City.id).all()
    # Print in format
    for city in cities:
        print("{}: ({}) {}".format(city.state, city.id, city.name))
    # Close the session
    my_session.close()
