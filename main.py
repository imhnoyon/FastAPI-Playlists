from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my first api"}



@app.get("/message")
def root():
    return {"message": "how are you"}



@app.post("/createposts")
def create_posts():
    return {"message":"successfully added your data"}