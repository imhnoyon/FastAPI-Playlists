from typing import Optional
from pydantic import BaseModel,EmailStr, Field # for import title str,content str
from datetime import datetime

class PostBase(BaseModel): # how many parameter we needed assign this function
    title: str
    content: str
    published: bool= True
    
    
class PostCreate(PostBase):
    pass



class Post(PostBase):
    id:int
    created_at:datetime
    owner_id:int

    class Config:  # Correct spelling
        orm_mode = True
    
    
    
class CreateUser(BaseModel):
    email:EmailStr
    password: str 
    
    
class UserOut(BaseModel):
    id:int
    email:EmailStr
    # password:str #ami password dekhate chai na ty eikhane likhi nai
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
        
class userLogin(BaseModel):
    email:EmailStr
    password:str
    
    
class token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[int] =None
    
    
    