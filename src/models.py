import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False, unique=True)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(2000), nullable=False)
    body = Column(String(2000), nullable=False)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    img_url = Column(String)
    user = relationship(Users)   


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(String(2000), nullable=False)
    posts = relationship(Posts)
    author = relationship(Users) 

class Followers(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_follower_id = Column(Integer, ForeignKey('users.id'))
    user_following_id = Column(Integer, ForeignKey('users.id'))
    follower = relationship(Users)


class Like(Base):
    __tablename__='Like'
    id = Column (Integer, primary_key=True)
    post_from_id = Column(Integer, ForeignKey('Post.id'))
    post_to_id = Column(Integer, ForeignKey('Post.id'))
    posts = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e