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
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""links""": ["""dh.com""","""https://github.com/Butakov-Andrey"""]}" http://127.0.0.1:8000/api/visited_links
  ```

### Авторизация пользователя:
* URL - http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
### Создание опроса:
  Если опрос активный - "is_active": true
* URL - http://127.0.0.1:8000/api/v1/polls/
### Редактирование опроса:
  Редактирование поля "started_at" запрещено, требуется указывать существующую дату
* URL - http://127.0.0.1:8000/api/v1/polls/[poll_id]/
### Создание вопроса:
* URL - http://127.0.0.1:8000/api/v1/questions/
### Редактирование вопроса:
* URL - http://127.0.0.1:8000/api/v1/questions/[question_id]/
### Создание ответа:
  Если пользователь авторизован, поле User можно оставить пустым, значение добавиться автоматически.  
  Если пользователь не авторизован, значением будет Token из COOKIES.  
  Можно указать значение пользователя вручную.  
* URL - http://127.0.0.1:8000/api/v1/answers/
### Редактирование ответа:
* URL - http://127.0.0.1:8000/api/v1/answers/[answer_id]/
### Получение списка активные опросов:
  "question_set" - список вопросов данного опроса
* URL - http://127.0.0.1:8000/api/v1/activepolls/
### Получение списка вопросов пользователя:
  user - id искомого пользователя
* URL - http://127.0.0.1:8000/api/v1/myanswers/?search=user
