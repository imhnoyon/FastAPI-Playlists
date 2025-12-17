from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel # for import title str,content str



app = FastAPI()




class Post(BaseModel): # how many parameter we needed assign this function
    title: str
    content: str
    








@app.get("/")
def root():
    return {"message": "Welcome to my first api"}



@app.get("/message")
def root():
    return {"message": "how are you"}



@app.post("/createposts")
def create_posts(playload: Post): #this post is class post name and parameter dictionary types and everything reacived in playload variable
    print(playload)
    return {f"Title -> {playload.title} Content -> {playload.content}"}