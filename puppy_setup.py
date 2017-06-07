import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

#will use when create mapper
from sqlalchemy.ext.declarative import declarative_base

#will use when create mapper
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'
    name = Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(String(10))
    website = Column(String)
    id = Column(Integer, primary_key = True)

class Puppy(Base):
    __tablename__ = 'puppy'
    name = Column(String(80), nullable = False)
    dateOfBirth = Column(Date)
    gender = Column(String(10), nullable = False)
    weight = Column(Numeric(10))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String)
    shelter = relationship(Shelter)
    id = Column(Integer, primary_key = True)

 
    
######insert at end of file########
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
