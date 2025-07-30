from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

os.makedirs("uploads", exist_ok=True)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})