import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    userid = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(15), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    idCharacter = Column(Integer, primary_key=True)
    name = Column(String(250))
    weight = Column(Integer)
    height = Column(Integer)
    planet_id = Column(ForeignKey('Planets.idPlanet'))

class Planets(Base):
    __tablename__ = 'Planets'
    idPlanet = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    Population = Column(Integer)
    sizeKm = Column(Float)
    Character = relationship('Characters')

    def to_dict(self):
        return {}

class Favorities(Base):
    __tablename__ = ' Favorities'
    favoriteId = Column(Integer, primary_key=True)
    userId = Column(ForeignKey('User.userId'))
    planetId = Column(ForeignKey('Planets.idPlanet'))
    characterId = Column(ForeignKey('Characters.idCharacter'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')