from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel # for import title str,content str


#connection with postgresql  codes here
import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='12345',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfully..")
        break
    except Exception as error:
        print("Connecting database fields")
        print("Error ", error)
        time.sleep(2)




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
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return{'data':posts}


#create post operation
from random import randint
@app.post("/posts")
def create_posts(post: Post): 
    
    cursor.execute(""" INSERT INTO posts (title,content, published) VALUES (%s , %s, %s) RETURNING * """ ,
                   (post.title,post.content, post.published))
    new_post=cursor.fetchone()
    conn.commit()
    
    return {"Data":new_post}    


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



#update any posts
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index=get_find_index(id)
    if index ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    
    post_dict = post.dict()
    post_dict['id']=id
    my_post[index] = post_dict
    print(post_dict)
    return {"data": post_dict}