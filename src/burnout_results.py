"""
CS3810: Principles of Database Systems
Instructor: Thyago Mota
Student(s): 
Description: Burnout Results
"""

import sys
from datetime import datetime
from helper_functions import get_db_params, yes_no_question, rate_question, date_question
from models import Base, BurnoutQuestion, Surveyee, Result
from sqlalchemy import create_engine, func
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

    # TODO #3: show the result of a burnout test previously applied to a surveyee on a specific date

    