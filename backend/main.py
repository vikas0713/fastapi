from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

import auth.authentication
from db import models
from db.database import engine
from routers import user, post


models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.authentication.router)

app.mount('/images', StaticFiles(directory='images'), name='images')


@app.get("/")
def root(param1=1):
    """
    Just returning Hello world from this view and also checking whether this description will be included in the
    document. I want to send this parameters from the view.
    @:param: param1
    :return: "Hello World"
    """
    return "Hello World"


