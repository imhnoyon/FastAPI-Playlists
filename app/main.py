from typing import Optional
from fastapi import Depends, FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel # for import title str,content str
app = FastAPI()




from .database import  engine,get_db
from . import models
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    return {"status":"Succesffuly"}



#connection with postgresql  codes here
from .secret_key import conn
import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        #  conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password',cursor_factory=RealDictCursor)
        conn=conn
        cursor = conn.cursor()
        print("Database connection was succesfully..")
        break
    except Exception as error:
        print("Connecting database fields")
        print("Error ", error)
        time.sleep(2)









class Post(BaseModel): # how many parameter we needed assign this function
    title: str
    content: str
    published: bool= True
    
    





#CRUD OPERATION 


#all post shown operation
@app.get('/posts')
def get_posts(db:Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()
    return{'data':posts}


#create post operation

@app.post("/posts")
def create_posts(post: Post,db:Session = Depends(get_db)): 
    
    # new_post= models.Post(title =post.title,content=post.content,published=post.published)
    
    #new efficient way to code bellow
    new_post= models.Post(**post.dict())
    
    #new something added or edit add this 3 line must
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return {"Data":new_post}    


#Single get post shown request
@app.get("/posts/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id: {id} was not found..")
    return {"post_details": post}






#delete post for indivual index
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db)):
    deleted_post=db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



#update any posts
@app.put("/posts/{id}")
def update_post(id:int, post:Post,db:Session=Depends(get_db)):
    
    update_post = db.query(models.Post).filter(models.Post.id == id)
    
    
    if update_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    update_post.update(post.dict(),synchronize_session=False)
    db.commit()
    

    return {"data": update_post.first()}