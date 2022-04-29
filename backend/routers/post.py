import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from auth.oauth import get_current_user
from db.database import get_db
from db.db_post import create, get, delete
from routers.schemas import PostBase, PostDisplay, UserAuth

router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types = ['absolute', 'relative']


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Invalid image type")
    return create(db, request)


@router.get('/all', response_model=List[PostDisplay])
def all_posts(db: Session = Depends(get_db)):
    return get(db)


@router.post('/image')
async def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    rand_str = ''.join(random.choice(letter) for i in range(6))
    filename = f'{image.filename.split(".")[0]}_{rand_str}.{image.filename.split(".")[1]}'
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": filename}


@router.delete('/{id}')
def delete_post(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return delete(db, id)
