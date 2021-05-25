from sqlalchemy.orm import Session

from app import schema, models


async def SaveUser(db: Session, userInfo: schema.User):
    user = models.User(**userInfo.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def getUsers(db: Session):
    return db.query(models.User).all()


async def deleteUser(db: Session, userInfo: schema.User):
    db.query().filter(models.User.id == userInfo.id).delete()
