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
    ``` json
    'NAME': 'tasksManagement',
    'USER': <name-user-postgresql>,
    'PASSWORD': <password-postgresql>
    ```
5. Load data from tasks.
    ``` 
    python manage.py loaddata tasks/fixture.json
    ```
6. Load data from users.
    ``` 
    python manage.py loaddata users/fixture.json
    ```

[Providing data with fixtures](https://docs.djangoproject.com/en/4.0/howto/initial-data/)

Dump app data to backup file
> python manage.py dumpdata --format=json tasks > tasks/fixture.json
> python manage.py dumpdata --format=json users > users/fixture.json

Load data backup
> python manage.py loaddata tasks/fixture.json
> python manage.py loaddata users/fixture.json