import requests


def parse_from_openweather(city: str) -> dict:
    API_KEY = '389fd44f904b18ef2ea61a8632c64256'
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}').json()


def parse_temp(data) -> float|str:
    if 'main' in data and 'temp' in data['main']:
        temp = data['main']['temp']
        return temp
    return 'надо сделать исключение по ключам погоды'




def parse(city: str) -> float:
    weather = parse_from_openweather(city=city)
    temp = parse_temp(data=weather)
    return temp


if __name__ == "__main__":
    print(parse(city="Moscow"))