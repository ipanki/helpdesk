# Helpdesk

## How to run

Configure environment variables:

```
cp .env.sample .env

```

Start services

```
docker-compose up -d postgres redis

```

Apply migrations

```
docker-compose run app python manage.py migrate
```

Start app

```
docker-compose up app
```

## How to run locally

Create virtual env:

```

python3 -m venv .venv

```

Activate virtual env:

```

. .venv/bin/activate

```

Install dependencies:

```

pip install -r requirements.txt

```

Start services:

```

docker-compose up -d postgres redis

```

Run migrations

```

python manage.py migrate

```

Create super user:

```

python manage.py createsuperuser

```

Configure environment variables:

```

cp .env.sample .env

```

Start celery worker:

```

celery -A helpdesk worker

```

Run server:

```

python manage.py runserver

```

## Urls

Access to admin: http://localhost:8000/admin/

Access to api: http://localhost:8000/api/

### Auth

Create access token: http://localhost:8000/api/token/

Refresh access token: http://localhost:8000/api/token/refresh/

### Issues

Manage issues: http://localhost:8000/api/issues/

## Run linter

```

make lint

```

## Sort imports

```

make imports

```

```

```
