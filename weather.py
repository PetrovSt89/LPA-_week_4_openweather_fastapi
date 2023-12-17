from fastapi import FastAPI

from config import city
from parse import parse


temp = parse()

app = FastAPI()

@app.get("/")
def weather():
    return {'приветствую друг': 'введи урл  /weather/'}


@app.get("/weather/")
def weather():
    return {city: temp}
