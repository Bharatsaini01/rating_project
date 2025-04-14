from fastapi import FastAPI, Request,Form,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from rating_project.database import engine,Session,sessionlocal
from rating_project import models,schemas
from typing import List
from rating_project.utils import avg_rating,rate_exp
import uvicorn,os


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="rating_project/templates")
app.mount("/static",StaticFiles(directory="rating_project/static"),name="static")

async def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse("rating.html",{"request":request})


@app.post("/")
async def add_rating(name : str = Form(...),rate : int = Form(...),db : Session = Depends(get_db)):
    new_rating = models.Rating(name = name,rate = rate)
    print(new_rating.name)
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return RedirectResponse(url ="/",status_code=303)

@app.get("/")
async def get_avg_rating(request: Request,db : Session = Depends(get_db)):
    rating = db.query(models.Rating.rate).all()
    avg_rate = avg_rating(rating)
    rating_exp = rate_exp(avg_rate) 
    return templates.TemplateResponse("rating.html",{"request":request,"avg_rating" : avg_rate,"rating_exp":rating_exp})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))