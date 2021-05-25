from fastapi import FastAPI, Depends
from . import   crud,models
from .database import SessionLocal, engine
from .schema import User

app = FastAPI(title="UserInfo")

models.Base.metadata.create_all(bind=engine)

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return {"Message": "Welcome"}

@app.get('/users')
async def getUsers(db=Depends(db)):
    return await crud.getUsers(db)

@app.post('/user')
async def CreateUser(user:User,db=Depends(db)):
    return await crud.SaveUser(db,user)


@app.delete("/user")
async  def DeleteUser(userId:int,db=Depends(db)):
    return await crud.deleteUser(db,userId)