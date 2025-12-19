from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .screct_file import SQLALCHEMY_DATABASE_URL

# SQLALCHEMY_DATABASE_URL ='postgresql://postgres:password@localhost/fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit = False ,autoflush=False ,bind=engine)

Base = declarative_base()

# Dependency → DB session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
