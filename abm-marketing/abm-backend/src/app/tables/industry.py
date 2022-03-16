from pydantic import BaseModel
from sqlalchemy import Column, String, Float, Integer
from app.db import Base

class IndustryCreate(BaseModel):
    name: str
    description: str

class Industry(IndustryCreate):
    id: int
    class Config:
        orm_mode = True

class IndustryModel(Base):
    __tablename__ = 'industry'
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    description= Column(String)
