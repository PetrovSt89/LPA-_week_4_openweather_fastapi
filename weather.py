from fastapi import FastAPI

from parse import parse


SITY = 'Moscow'

temp = parse(SITY)

app = FastAPI()


@app.get("/")
def weather():
    return {'приветствую друг': 'введи урл  /weather/'}


@app.get("/weather/")
def weather():
    return {SITY: temp}
