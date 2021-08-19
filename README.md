# dockerized-django-gunicorn-nginx-psql-template
Template for easy running django app served by nginx + gunicorn with postgres as database


## How to setup
1. `git clone https://github.com/berryrock/dockerized-django-gunicorn-nginx-psql-template.git`

2. Create file `.env` and fill it with next variables:
- DEBUG


- ALLOWED_HOSTS

    With space as divider. Default allowed all hosts


- SECRET_KEY

    Django app secret key. Without default value


- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD

    To setup default psql in docker and connect it with Django.

    Required. As default use `postgres` as value.


- POSTGRES_HOST=db
- POSTGRES_PORT=5432


3. Prepare docker volumes for Postgres:
```
docker volume create --name=pgdata_for_main_app
```

4. Give permissions to execute entrypoint file for Django app
```
chmod +x entrypoint.sh
```

5. Build and run:
```
docker-compose build
docker-compose up
```

6. Enjoy!

***

[Author](http://berryrock.ru/)
