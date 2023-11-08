import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(50),nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    
    

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_type = Column(String(100), nullable=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)
    user = relationship(User)


class Likes(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey("comment.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    comment = relationship(Comment)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e