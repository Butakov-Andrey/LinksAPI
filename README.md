# LinksAPI
Web-приложения для учета посещенных ссылок
### Функционал системы:
* JSON API по HTTP
* Ресурс загрузки посещений в виде массива ссылок
* Ресурс получения списка уникальных доменов, посещенных за переданный интервал времени
* Хранение данных в Redis 
## Использованные технологии:
* Django
* Django REST framework
* Redis
* Docker
## Установка и запуск:
0. Запускаем Redis в контейнере Docker:
  ```
  ...\> docker pull redis
  ...\> docker run --name myredis -p 6379:6379 -d redis
  ```
1. Клонируем репозиторий и заходим в директорию:
  ```
  ...\> git clone https://github.com/Butakov-Andrey/LinksAPI.git
  ...\> cd LinksAPI
  ```
2. Создаем виртуальное окружение и активируем его:
  ```
  ...\> python -m venv env
  ...\> env\scripts\activate
  ```
3. Устанавливаем зависимости из requirements.txt:
  ```
  ...\> pip install -r requirements.txt
  ```
4. Запускаем миграции:
  ```
  ...\> manage.py migrate
  ```
5. Запускаем приложение:
  ```
  ...\> manage.py runserver
  ```
Приложение доступно по адресу http://127.0.0.1:8000/
## Использование:
Документация API:
* Swagger - http://127.0.0.1:8000/swagger/
* Redoc - http://127.0.0.1:8000/redoc/
### Загрузка посещений:
* URL - http://127.0.0.1:8000/api/visited_links
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""links""": ["""dh.com""","""https://github.com/Butakov-Andrey"""]}" "http://127.0.0.1:8000/api/visited_links"
  ```
### Получение списка уникальных доменов:
* URL - http://127.0.0.1:8000/api/visited_domains/
* curl:
  ```
  ...\> curl http://127.0.0.1:8000/api/visited_domains/
  ```
### Получение списка уникальных доменов за переданный интервал времени:
* URL - http://127.0.0.1:8000/api/visited_domains/?from=0900221230&to=1100217603
  (время указывается без разделителей, десять цифр)
* curl:
  ```
  ...\> curl "http://127.0.0.1:8000/api/visited_domains/?from=0900221230&to=1100217603"
  ```
### Запуск тестов:
  ```
  ...\> manage.py test
  ```
