# Media Profit Quality Task

## Setup

1. `git clone` project
2. Make sure you have installed `Python` in your machine, by running `python -v` in terminal. If you don't see version of your `python` install it from here [install python](https://www.python.org/downloads)
3. Install `pipenv` by running `pip install pipenv`
4. Run `pipenv install` to install all dependencies from `Pipfile` and `Pipfile.lock`
5. Execute `pipenv shell` for shell mode
6. Copy `.env` variables from `.env.sample`
7. Setup `.env` variables (DJANGO_SECRET_KEY) situated in `credentials.txt`. Set your superuser username, email and password for admin panel accessability
8. Run `cd test_task`
9. Execute `python manage.py makemigrations`
10. Execute `python manage.py migrate`
11. To start server and django app run `python manage.py runserver`

Endpoint for spend app `http://localhost:8080/spend`
Endpoint for revenue app `http://localhost:8080/revenue`
