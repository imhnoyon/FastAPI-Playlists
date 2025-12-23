

from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import  engine,get_db
from .. import models,schema

router=APIRouter(
    tags=['Users']
)


#register user
from passlib.context import CryptContext
pwd_context = CryptContext( schemes=["bcrypt"], deprecated="auto")

@router.post("/users",status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
def Create_user(user:schema.CreateUser,db:Session=Depends(get_db)):
    #hashing the password
    
    hashed_password = pwd_context.hash(user.password)
    user.password=hashed_password
    new_user=models.User(email=user.email,
        password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
    
#get shown one user by id

@router.get("/users/{id}",response_model=schema.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    
    user=db.query(models.User).filter(models.User.id == id).first()
    
    if user == None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    return user


@router.get("/users",response_model=List[schema.UserOut])
def get_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users
    
    