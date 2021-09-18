# opros_api
/Django 2.2.10, Django REST framework API, SQLITE/

upd. Сломал внешний вид админки и всего прочего, на функционале не должно сказаться, фикшу

## Установка
*cmd*

- pip install Django==2.2.10

- pip install django-grappelli

- pip install markdown  

- pip install djangorestframework

- pip install pyyaml

- pip install django-filter 

# Скопировать репозиторий через GIT
или скачать архив, далее перейти в папку OPROS_API через cd
![image](https://user-images.githubusercontent.com/82372152/133359918-9487065b-0f14-455c-a83e-c754e460cab6.png)




https://github.com/Shk337/oprosapi

Далее перейти через cmd в папку OPROSAPI (там где лежит файл manage.py)

- pip install -r requirements.txt

создать миграции

- python manage.py makemigrations
- python manage.py migrate

создаем пользователя (логин, пароль и подтверждение)
- python manage.py createsuperuser
 
 Запускаем сервер, который будет иметь адрес http://localhost:8000/
 
 - python manage.py runserver

# Получение токена пользователя 
http://localhost:8000/api/login/


Bash запрос:
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=ИМЯ ПОЛЬЗОВАТЕЛЯ КОТОРОЕ МЫ СОЗДАЛИ РАНЕЕ' \
--form 'password=ПАРОЛЬ ПОЛЬЗОВАТЕЛЯ'
```
# Создание вопроса
http://localhost:8000/api/question/create/

Токен указывается, тот который мы получили ранее или создали в Админ-панели , например, 207c25e8b8e5caa4ccf5152cf6780842eb21514b

Bash запрос:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token ТУТ_УКАЗЫВАТЕСЯ ТОКЕН' \
--form 'survey=ОПРОС' \
--form 'question_text=ТЕКСТ ВОПРОСА' \
--form 'question_type=ТИП ВОПРОСА \
```

# Обновляем вопрос:
http://localhost:8000/api/question/update/НОМЕР ВОПРОСА/

В  URL нужно вставить ID вопроса ↑

Bash запрос:
```
curl --location --request POST 'http://localhost:8000/api/question/update/НОМЕР ВОПРОСА' \
--header 'Authorization: Token ТУТ_УКАЗЫВАТЕСЯ ТОКЕН' \
--form 'survey=ОПРОС' \
--form 'question_text=ТЕКСТ ВОПРОСА' \
--form 'question_type=ТИП ВОПРОСА \
```
# Удаление вопроса:
http://localhost:8000/api/question/update/НОМЕР ВОПРОСА/

Bash запрос по аналогии

# Cоздание опроса:
http://localhost:8000/api/surveysApp/create/

!Дата указывается в формате 2012-09-04 06:00 

Bash запрос:
```
curl --location --request POST 'http://localhost:8000/api/surveysApp/create/' \
--header 'Authorization: Token ТУТ УКАЗЫВАЕТСЯ ТОКЕН' \
--form 'survey_name=ИМЯ ОПРОСА' \
--form 'pub_date=ДАТА ПУБЛИКАЦИИ' \
--form 'end_date=ОКОНЧАНИЕ ПУБЛИКАЦИИ \
--form 'survey_description=ОПИСАНИЕ ОПРОСА'
```

# Обновление опроса:
http://localhost:8000/api/surveysApp/update/НОМЕР ОПРОСА/

!Дата указывается в формате 2012-09-04 06:00 

Bash запрос по аналогии выше:

# Удаление опроса:
http://localhost:8000/api/surveysApp/update/НОМЕР ОПРОСА/

!Дата указывается в формате 2012-09-04 06:00 

Bash запрос:
```
curl --location --request DELETE 'http://localhost:8000/api/surveysApp/update/НОМЕР ОПРОСА/' \
--header 'Authorization: Token ТОКЕН ПОЛЬЗОВАТЕЛЯ'
```

# Посмотреть все опросы:
http://localhost:8000/api/surveysApp/view/

Bash запрос:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/' \
--header 'Authorization: Token ТОКЕН ПОЛЬЗОВАТЕЛЯ'
```

# Посмотреть активных запросов:
http://localhost:8000/api/surveysApp/view/active/

Bash запрос:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/active/' \
--header 'Authorization: Token ТОКЕН ПОЛЬЗОВАТЕЛЯ'
```

# Создание выбора:
http://localhost:8000/api/choice/create/

Bash запрос:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token Токен Пользователя' \
--form 'question=Вопрос' \
--form 'choice_text=Текст выбора'
```

# Обновление выбора:
http://localhost:8000/api/choice/update/НОМЕР ВЫБОРА/

Bash запрос:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token Токен Пользователя' \
--form 'question=Вопрос' \
--form 'choice_text=Текст выбора'
```
# Удаление выбора:
http://localhost:8000/api/choice/update/НОМЕР ВЫБОРА/

Bash запрос:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/Номер ВЫБОРА/' \
--header 'Authorization: Token ТОКЕН ПОЛЬЗОВАТЕЛЯ' \
--form 'question=ВОПРОС' \
--form 'choice_text=ТЕКСТ ВЫБОРА'
```

# Создание, удаление и обновление ответов пользователей происходят по аналогии с командами выше
http://localhost:8000/api/answer/create/

http://localhost:8000/api/answer/update/НОМЕР ОТВЕТА/      ( для обновления и удаления, после создания вопроса)


# Просмотр всех ответов

http://localhost:8000/api/answer/view/НОМЕР ПОЛЬЗОВАТЕЛЯ/

Bash запрос:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/НОМЕР ПОЛЬЗОВАТЕЛЯ' \
--header 'Authorization: Token Токен пользователя'
```


Узнать метод запроса можно по командам: GET, DELETE, PATCH, POST соответственно их функциям. Получения информации, удаления, обновления и принятия данных.
