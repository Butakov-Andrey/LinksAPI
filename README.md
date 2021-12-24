# LinksAPI
Web-приложения для учета посещенных ссылок
### Функционал для администратора системы:
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
2. Клонируем репозиторий и заходим в директорию:
  ```
  ...\> git clone https://github.com/Butakov-Andrey/PollAPI.git
  ...\> cd PollAPI
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
4. Создаем миграции:
  ```
  ...\> manage.py makemigrations polls
  ...\> manage.py migrate
  ```
5. Создаем суперпользователя:
  ```
  ...\> manage.py createsuperuser
  Username (leave blank to use 'admin'): admin
  Email address: admin@admin.com
  Password: ********
  Password (again): ********
  Superuser created successfully.
  ```
6. Запускаем приложение:
  ```
  ...\> manage.py runserver
  ```
Приложение доступно по адресу http://127.0.0.1:8000/
## Использование:
Документация API:
* Swagger - http://127.0.0.1:8000/swagger/
* Redoc - http://127.0.0.1:8000/redoc/
### Создание пользователя:
* URL - http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
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
