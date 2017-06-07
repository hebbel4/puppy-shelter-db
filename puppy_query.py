from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from puppy_setup import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query1():
    """Query all of the puppies and return the results
    in ascending alphabetical order"""
    puppies = session.query(Puppy).order_by(Puppy.name).all()
    for p in puppies:
        print p.name

#query1()

def query2():
    """Query all of the puppies that are less than 6 months old
    organized by the youngest first"""
    current_time = datetime.date.today()
    six_months_ago = current_time - datetime.timedelta(days = 182)
    results = session.query(Puppy.name, Puppy.dateOfBirth)\
              .filter(Puppy.dateOfBirth >= six_months_ago)\
              .order_by(Puppy.dateOfBirth.desc()).all()
    for item in results:
        print "{name} : {birthday}".format(name = item.name, birthday = item.dateOfBirth)

#query2()

def query3():
    """Query all puppies by ascending weight"""
    results = session.query(Puppy).order_by(Puppy.weight).all()
    for item in results:
        print "{name} : {weight}".format(name = item.name, weight = item.weight)

#query3()

def query4():
    """Query all puppies grouped by the shelter in which they are staying"""
    result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Puppy.shelter_id).all()
    for item in result:
        print item[0].id, item[0].name, item[1]

#query4()
    
