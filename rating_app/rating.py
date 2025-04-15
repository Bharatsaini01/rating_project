from fastapi import FastAPI, Request,Form,Depends
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from rating_project.database import engine,Session,sessionlocal
from rating_project import schemas
from typing import List
from rating_project.utils import avg_rating,rate_exp
from rating_project.crud import *
import uvicorn,os


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="rating_project/templates")
app.mount("/static",StaticFiles(directory="rating_project/static"),name="static")


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
    ratings = rating(db)
    avg_rate = avg_rating(ratings["ratings"])
    total_rating = ratings["tatal_rating"]
    return templates.TemplateResponse("rating.html",{"request":request,"avg_rating" : avg_rate,"total_rating":total_rating})

if __name__ == "__main__":
    uvicorn.run("rating:app", host="127.0.0.1", port=int(os.environ.get("PORT", 10000)))
