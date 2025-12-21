import psycopg2
from psycopg2.extras import RealDictCursor
import time        
conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='12345',cursor_factory=RealDictCursor)

SQLALCHEMY_DATABASE_URL ='postgresql://postgres:12345@localhost/fastapi'