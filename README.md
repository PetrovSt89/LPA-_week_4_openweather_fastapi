# Проект Weather

Weather - это веб приложение, которое показывает температуру в определенном городе.

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение
3. Создайте файл .env и создайте в нем переменные:
    ```
    API_KEY = "Ключ api openweathermap.org"
    CITY = "Город, в котором хотите узнать температуру"
    ```
4. Соберите образ командой:
    ```
    docker build --tag weather .
    ```
6. Запустите образ, передайте переменные окружения, пропишите порт
    командой:
    ```
    docker run --env-file=.env -p 8000:80 weather
    ```