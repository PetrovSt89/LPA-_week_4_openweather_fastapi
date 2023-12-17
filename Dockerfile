FROM python:3.10-alpine

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "weather:app", "--host", "0.0.0.0", "--port", "80"]
