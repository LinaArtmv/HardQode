# Тестовое задание для HardQode

### Tехнологии
- [Python 3.10](https://www.python.org/downloads/)
- [Django 4.2](https://www.djangoproject.com/)
- [Django Rest Framewok 3.14](https://www.django-rest-framework.org/)


### Локальный запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

``` git@github.com:LinaArtmv/HardQode.git ``` 
``` cd HardQode ``` 

Создать и активировать виртуальное окружение:

``` python3 -m venv venv ``` 
``` source venv/bin/activate ```     
``` python3 -m pip install --upgrade pip ``` 

Установить зависимости из файла requirements:

``` pip install -r requirements.txt ``` 

Выполнить миграции:

``` python3 manage.py migrate ```

Загрузить тестовые данные:

``` python3 manage.py loaddata db.json ```

Запустить проект:

``` python3 manage.py runserver ``` 


### Примеры запросов к API и ответов от сервера

- Пример GET-запроса на адрес http://127.0.0.1:8000/api/lessons/: 
```
[
    {
        "lesson": "Урок ООП",
        "length": 500,
        "status": "Просмотрено"
    },
    {
        "lesson": "Урок CSS",
        "length": 400,
        "status": "Не просмотрено"
    }
]
```

- Пример GET-запроса на адрес http://127.0.0.1:8000/api/products/product_id/lessons/:

```
{
    "lesson": "Урок ООП",
    "length": 500,
    "status": "Просмотрено",
    "date": "2023-09-25"
}
```

- Пример GET-запроса на адрес http://127.0.0.1:8000/api/products/statistic/: 
```
[
    {
        "name": "Python-разработчик",
        "count_lesson": 1,
        "summ_length": 1000,
        "count_user": 1,
        "product_purchases": 50.0
    },
    {
        "name": "Frontend-разработчик",
        "count_lesson": 1,
        "summ_length": 800,
        "count_user": 1,
        "product_purchases": 50.0
    }
]
```

### Автор проекта
- Ангелина Артемьева,
github: [LinaArtmv](https://github.com/LinaArtmv)