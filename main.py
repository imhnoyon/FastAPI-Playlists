from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel # for import title str,content str



app = FastAPI()




class Post(BaseModel): # how many parameter we needed assign this function
    title: str
    content: str
    published: bool= True
    rating: Optional[int] = None # optional field
    



def find_post(id):
    for p in my_post:
        if p['id'] == int(id):
            print(p)
            return p
        
        
def get_find_index(id):
    for i,p in enumerate(my_post):
        if p['id'] ==int(id):
            return i




@app.get("/")
def root():
    return {"message": "Welcome to my first api"}



@app.get("/message")
def root():
    return {"message": "how are you"}


# @app.post("/posts")
# def create_posts(playload: Post): #this post is class name post and parameter dictionary types and everything reacived in playload variable
#     print(playload)
#     print(playload.dict())
#     my_post.append(playload.dict())
#     return {"Data":my_post}





#CRUD OPERATION 

my_post = [
    {'title': 'Title of post 1', 'content': 'Content of post 1', 'id': 1},
    {'title': 'Title of post 2', 'content': 'Content of post 2', 'id': 2},
    {'title': 'Title of post 3', 'content': 'Content of post 3', 'id': 3},
    {'title': 'Title of post 4', 'content': 'Content of post 4', 'id': 4},
    {'title': 'Title of post 5', 'content': 'Content of post 5', 'id': 5},
    {'title': 'Title of post 6', 'content': 'Content of post 6', 'id': 6},
    {'title': 'Title of post 7', 'content': 'Content of post 7', 'id': 7},
    {'title': 'Title of post 8', 'content': 'Content of post 8', 'id': 8},
    {'title': 'Title of post 9', 'content': 'Content of post 9', 'id': 9},
    {'title': 'Title of post 10', 'content': 'Content of post 10', 'id': 10}
]


#all post shown operation
@app.get('/posts')
def get_posts():
    return{'data':my_post}


#create post operation
from random import randint
@app.post("/posts")
def create_posts(playload: Post): 
    post_dict = playload.dict()
    post_dict['id'] = randint(10,1000)
    my_post.append(post_dict)
    return {"Data":my_post}    


#Single get post shown request

#leatest post find
@app.get ("/posts/leatest")
def get_leatest_post():
    post = my_post[len(my_post)-1]
    return {'data':post}

@app.get("/posts/{id}")
def get_post(id):
    post=find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post of id: {id} was not found..")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'message':f"Post of id: {id} was not found.."}
    return {"post_details": post}






#delete post for indivual index
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id= int):
    index=get_find_index(id)
    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)