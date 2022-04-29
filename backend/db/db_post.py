from datetime import datetime

from sqlalchemy.orm import Session

from db.models import DbPost
from routers.schemas import PostBase


def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get(db: Session):
    return db.query(DbPost).all()


def delete(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    db.delete(post)
    db.commit()
    return {"message": "ok"}

