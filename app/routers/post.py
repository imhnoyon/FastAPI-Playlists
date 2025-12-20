
from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import  engine,get_db
from .. import models,schema



router=APIRouter(
    tags=['Posts']
)


#CRUD OPERATION 


#all post shown operation
@router.get('/posts',response_model=List[schema.Post])
def get_posts(db:Session = Depends(get_db)):
    
    posts = db.query(models.Post).all()
    return posts



#create post operation

@router.post("/posts",response_model=schema.Post)
def create_posts(post: schema.PostCreate,db:Session = Depends(get_db)): 
    
    # new_post= models.Post(title =post.title,content=post.content,published=post.published)
    
    #new efficient way to code bellow
    new_post= models.Post(**post.dict())
    
    #new something added or edit add this 3 line must
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


#Single get post shown request
@router.get("/posts/{id}",response_model=schema.Post)
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id: {id} was not found..")
    return  post






#delete post for indivual index
@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db)):
    deleted_post=db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



#update any posts
@router.put("/posts/{id}",response_model=schema.Post)
def update_post(id:int, post:schema.PostCreate,db:Session=Depends(get_db)):
    
    update_post = db.query(models.Post).filter(models.Post.id == id)
    
    
    if update_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    update_post.update(post.dict(),synchronize_session=False)
    db.commit()
    

    return  update_post.first()