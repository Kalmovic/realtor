from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random
import string

Base = declarative_base()
# This secret key will be used to create and verify your tokens
secret_key = ''.join(
    random.choice(
        string.ascii_uppercase +
        string.digits) for x in xrange(32))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id,
        }


class Immobile(Base):
    __tablename__ = 'immobile'

    address = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)
    squarefeet = Column(String(20), nullable=False)
    bedrooms = Column(String(20), nullable=False)
    bathrooms = Column(String(20), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship(City)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'address': self.address,
            'description': self.description,
            'id': self.id,
            'squarefeet': self.squarefeet,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'user_id': self.user_id,
        }


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})


Base.metadata.create_all(engine)
