from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    login: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
