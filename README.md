# tasksManagement

### Configure environment 

1. Configure virtual environment and activate it.
    ``` 
    python -m venv myvenv
    myvenv\Scripts\activate
    ```
2. Install pip.
    ``` 
    python -m pip install -- upgrade pip
    ```
3. Install required packages.
    ``` 
    pip install -r requirements.txt
    ```
4. Create database in Postgresql and configure [tasksManagement/settings.py](./tasksManagement/settings.py).
    ```
    'NAME': 'tasksManagement',
    'USER': <name-user-postgresql>,
    'PASSWORD': <password-postgresql>
    ```
5. Make migrations and migrate for database.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Load data from tasks (optional).
    ``` 
    python manage.py loaddata tasks/fixture.json
    ```
7. Load data from users (optional).
    ``` 
    python manage.py loaddata users.json
    ```

[Providing data with fixtures](https://docs.djangoproject.com/en/4.0/howto/initial-data/)

Dump app data to backup file
> python manage.py dumpdata --format=json tasks > tasks/fixture.json
> python manage.py dumpdata auth > users.json

Load data backup
> python manage.py loaddata tasks/fixture.json
> python manage.py loaddata users.json