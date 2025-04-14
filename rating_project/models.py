from sqlalchemy import Column, Integer, String
from database import *

class Rating(Base):
   __tablename__ = 'Rating'

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String(50))
   rate = Column(Integer)