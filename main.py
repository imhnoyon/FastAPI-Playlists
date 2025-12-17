from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel # for import title str,content str



app = FastAPI()




class Post(BaseModel): # how many parameter we needed assign this function
    title: str
    content: str
    published: bool= True
    rating: Optional[int] = None # optional field
    








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
def find_post(id):
    for p in my_post:
        if p['id'] == int(id):
            print(p)
            return p

@app.get("/posts/{id}")
def get_post(id):
    post=find_post(int(id))
    return {"post_details": post}