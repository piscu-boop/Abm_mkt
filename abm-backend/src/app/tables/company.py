from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from app.db import Base

class CompanyCreate(BaseModel):
    name: str
    web: str

class Company(CompanyCreate):
    id: int
    class Config:
        orm_mode = True

class CompanyModel(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    web = Column(String)
