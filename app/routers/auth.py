from fastapi import FastAPI,Depends,status,Response,APIRouter,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. schema import userLogin
from .. import models,utils,auth2
router=APIRouter(tags=['Authentications'])


@router.post("/login")
def user_login(Credentials:userLogin, db:Session=Depends(get_db)):
    
    user= db.query(models.User).filter(models.User.email == Credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    if not utils.varify(Credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    
    
    #create jwt token bellow
    access_token = auth2.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}
        
    
    
