Installation methods
================
#Docker way
Run `docker-compose up` and `docker-compose run web ./manage.py migrate`

You  can change setup config in file .env in `config` folder.

#Poetry way 
Run `poetry install` and check database configuration in `config/.env` file

# Pip way
There is also requirements.txt for pip users.
I suggest to use virtualenv instead setup on bare os.

`pip install -r requirements.txt`


