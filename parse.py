import requests

from config import api_key, city


def parse_from_openweather() -> dict:
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').json()


def parse_temp(data) -> float|str:
    if 'main' in data and 'temp' in data['main']:
        temp = data['main']['temp']
        return temp
    return 'надо сделать исключение по ключам погоды'




def parse() -> float:
    weather = parse_from_openweather()
    temp = parse_temp(data=weather)
    return temp


if __name__ == "__main__":
    print(parse(city))