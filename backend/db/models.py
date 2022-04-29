from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class DbUser(Base):
    __tablename__: str = "user"

    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username: str = Column(String)
    email: str = Column(String)
    password: str = Column(String)
    posts = relationship('DbPost', back_populates='user')



class DbPost(Base):
    __tablename__: str = "post"
    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_url: str = Column(String)
    image_url_type: str = Column(String)
    caption: str = Column(String)
    timestamp: datetime = Column(DateTime)
    user_id: int = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='posts')
