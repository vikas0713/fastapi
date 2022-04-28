from sqlalchemy.orm import Session

from db.hashing import Hash
from db.models import DbUser
from routers.schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.hash_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
