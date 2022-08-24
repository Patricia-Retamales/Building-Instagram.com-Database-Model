import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)



class User(Base):
    __tablename__='user'
    id= Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Follower(Base):
    __tablename__='follower'
    user_from_id= Column(Integer, ForeignKey('user.id'),primary_key=True)
    user_to_id= Column(Integer, ForeignKey('user.id'),primary_key=True)
    relationUser = relationship(User)


class Comment(Base):
    __tablename__='comment'
    id= Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id=Column(Integer, ForeignKey('user.id'))
    post_id=Column(Integer, ForeignKey('post.id'))
    relationUser = relationship(User)

class Post(Base):
    __tablename__='post'
    id= Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    relationComment =relationship(Comment)

class Media(Base):
    __tablename__='media'
    id= Column(Integer, primary_key=True)
    enum = Column(String(250))
    url = Column(String(250))
    post_id=Column(Integer, ForeignKey('post.id'))


class Publicidad(Base):
    __tablename__='publicidad'
    id= Column(Integer, primary_key=True)
    url = Column(String(250))
    title= Column(String(250))
    title_id=Column(Integer, ForeignKey('user.id')) 



class Seguir(Base):
    __tablename__='seguir'
    id= Column(Integer, primary_key=True)
    seguidores= Column(String(250))
    seguidores_id=Column(Integer, ForeignKey('user.id'))
    relationUser = relationship(User)


class Historia(Base):
    __tablename__='historia'
    id= Column(Integer, primary_key=True)
    url= Column(String(250))
    url_id=Column(Integer, ForeignKey('user.id'))
    relationUser = relationship(User)

class Tienda(Base):
    __tablename__='tienda'
    id= Column(Integer, primary_key=True)
    nombre_de_obj=Column(String(250))
    url= Column(String(250))
    url_id=Column(Integer, ForeignKey('user.id'))
    relationUser = relationship(User)
    relationFollower = relationship(Follower)
    relationHistoria = relationship(Historia)



    def to_dict(self):
        return {}









## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e