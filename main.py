from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my first api"}



@app.get("/message")
def root():
    return {"message": "how are you"}



@app.post("/createposts")
def create_posts(playload: dict =Body(...)): #parameter dictionary types and everything reacived in playload variable
    print(playload)
    return {"message":f"Course: {playload['name']} Instractor: {playload['instractor']} Duration:{playload['duration']} "}