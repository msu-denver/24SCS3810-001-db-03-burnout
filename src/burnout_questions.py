"""
CS3810: Principles of Database Systems
Instructor: Thyago Mota
Student(s): 
Description: Questions Upload
"""

import sys
from helper_functions import get_db_params
from models import Base, BurnoutQuestion, Surveyee, Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__": 

    # connection to the database (make sure postgres is running!)
    params = get_db_params()
    engine = create_engine(f"postgresql://{params['user']}:{params['passwd']}@{params['host']}:{params['port']}/{params['dbname']}")
    if not engine: 
        print('Couldn\'t conect to the database!')
        sys.exit(1)
    Session = sessionmaker(engine)
    session = Session()

    # tables creation from the model
    Base.metadata.create_all(engine)

    # TODO #1: read the questions in data/questions.txt one at a time, instantiate an object of type BurnoutQuestion and save it in the database
