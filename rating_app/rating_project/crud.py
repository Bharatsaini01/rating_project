from rating_project import models
from rating_project.database import Session,sessionlocal
from fastapi import Depends



async def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

def rating(db):
    ratings = db.query(models.Rating.rate).all()
    total_rating = len(ratings)
    data = {
        "ratings":ratings,
        "tatal_rating":total_rating
    }
    return data