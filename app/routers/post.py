
from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from typing import List
from sqlalchemy.orm import Session
from ..database import  engine,get_db
from .. import models,schema,auth2



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
def create_posts(post: schema.PostCreate,db:Session = Depends(get_db),get_current_user:int = Depends(auth2.get_current_user)): 
    
    # new_post= models.Post(title =post.title,content=post.content,published=post.published)
    
    #new efficient way to code bellow
    new_post= models.Post(**post.dict(),owner_id=get_current_user.id)
    
    #new something added or edit add this 3 line must
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post


#Single get post shown request
@router.get("/posts/{id}",response_model=schema.Post)
def get_post(id:int,db:Session=Depends(get_db),get_current_user:int = Depends(auth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id: {id} was not found..")
    return  post






#delete post for indivual index
@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db),get_current_user:int = Depends(auth2.get_current_user)):
    deleted_post_query=db.query(models.Post).filter(models.Post.id == id)
    
    post=deleted_post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    if post.owner_id !=get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized to perfrom the request")
    
    deleted_post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



#update any posts
@router.put("/posts/{id}",response_model=schema.Post)
def update_post(id:int, post:schema.PostCreate,db:Session=Depends(get_db),get_current_user:int = Depends(auth2.get_current_user)):
    
    update_post = db.query(models.Post).filter(models.Post.id == id)
    
    
    if update_post.first() ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    if update_post.first().id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Not Authorized to perfrom the request")
    
    update_post.update(post.dict(),synchronize_session=False)
    db.commit()
    

    return  update_post.first()