from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    contact: str

    class Config:
        orm_mode = True
