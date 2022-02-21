# API REST Hero

## Introduction

This is a simple API REST made with **django** and **django-rest-framework**. It allows the basic CRUD operations using the embedded **sqlite** database.

## Setup

All modules are in in `requirements.txt` file, so once you have downloaded the repo, simple run:

```bash
pip install -r requirements.txt
```

### Admin user
A default admin user was created with username *admin* and password *Palabra123$*

After that, run:

```bash
python manage.py makemigrations
```

and:
```bash
python manage.py migrate
```

And finally, you can start the server with:

```bash
python manage.py runserver
```

## Endpoints

- **POST** `/heroapi`: Create a new hero.

```json
{
    "name": "Aquaman",
    "alias": "Lord of the water"
}
```

- **GET** `/heroapi`: Return all heroes available.
Example response:
```json
{
    "id": 1,
    "name": "Aquaman",
    "alias": "Lord of the water"
}
```

- **GET** `/heroapi/id`: Return a hero based on id.
Example response:
```json
[
    {
        "id": 1,
        "name": "Aquaman",
        "alias": "Aqua"
    },
    {
        "id": 2,
        "name": "Capitan America",
        "alias": "El capi"
    },
    {
        "id": 3,
        "name": "Flash",
        "alias": "Bolt"
    }
]
```

- **PUT** `/heroapi/id`: Update a hero. It allows partial modifications.
```
{
    "alias": "The fastest"
}
```

- **DELETE** `/heroapi/id`: Delete a hero.

## Tools


- Django
- django-rest-framework
- sqlite3