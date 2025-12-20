from typing import Optional,List
from fastapi import Depends, FastAPI,Response,status,HTTPException
from fastapi.params import Body


from .database import  engine,get_db
from . import models,schema
from sqlalchemy.orm import Session

from .routers import post,user,auth

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




models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

