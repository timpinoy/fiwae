# Project Description
This is a first project with Django to get some understanding of how it works.
It's very basic to load in CSV files from [KBC](https://kbc.be) accounts and to get an overview.

# Prereqisites
Make sure the following are installed
```
pip install django
pip install django-bootstrap-v5
pip install djangorestframework
```

Afterwards from the main directory run the below and make your user
```
python manage.py migrate
python manage.py createsuperuser
```
# Run
Start the server with
```
python manage.py runserver
```
Browse to [http://127.0.0.1:8000/finance/](http://127.0.0.1:8000/finance/)

# Other
Bootstrap theme used: [SB Admin](https://startbootstrap.com/template/sb-admin)
