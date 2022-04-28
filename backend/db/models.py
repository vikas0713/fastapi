from sqlalchemy import Column, Integer, String

from .database import Base


class DbUser(Base):
    __tablename__: str = "user"

    id: int = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username: str = Column(String)
    email: str = Column(String)
    password: str = Column(String)


