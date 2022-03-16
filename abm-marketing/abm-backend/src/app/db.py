from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DOCKER_DATABASE_URL = os.getenv("DATABASE_URL")

''' 
    Docker vs Local running model
'''
if DOCKER_DATABASE_URL:
    engine = create_engine( DOCKER_DATABASE_URL )
else:
    # engine = create_engine("postgresql://postgres:@localhost:5432/postgres")
    engine = create_engine("postgresql://postgres:Abrilb30!@localhost:5432/abm_backend")
    # engine = create_engine("mysql+mysqlconnector://root:Abrilb30!@localhost:3306/abm")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

''' DB Session '''
def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()