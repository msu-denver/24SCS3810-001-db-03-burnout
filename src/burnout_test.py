"""
CS3810: Principles of Database Systems
Instructor: Thyago Mota
Student(s): 
Description: Test Application
"""

import sys
from datetime import datetime
from helper_functions import get_db_params, yes_no_question, rate_question
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

    # TODO #2: apply a burnout test to a surveyee and save the test results in the database; you should also save the surveyee's information if it is the first time that the test is being administered to them

    