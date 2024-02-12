from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from dependencies import get_db
import auth

app = FastAPI()
app.include_router(auth.router)


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/", status_code=status.HTTP_200_OK)
def get_user(db: db_dependency, user: None):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return {"User": 1}
