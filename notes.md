* Diretory Structure:
  * `__init.py__`: a special file that tells python to treat this directory like a python package.
  * `asgi.py`, `wsgi.py`: special configuration files, allows django to communicate with web servers.
  * `settings.py`: configurations like Databases
  * `urls.py`
  * `manage.py`: a special config file
    * acts like a command line tool
    * allows us to do things like make database migration, run our Python server

### Django App

* Django app: a standalone application that can be plugged in a Django project.

* Create an app:

  1. `python .\manage.py startapp myapp`

  2. link this app to the Django project, in the `settings.py`:

     ```python
     INSTALLED_APPS = [
         "django.contrib.admin",
         "django.contrib.auth",
         "django.contrib.contenttypes",
         "django.contrib.sessions",
         "django.contrib.messages",
         "django.contrib.staticfiles",
         "myapp"
     ]
     ```

* configure urls:

  * in the `urls.py` file of an application: match the url for each function:

    ```python
    from django.urls import path
    from . import views
    
    urlpatterns = [
        # match '' to the views.home function
        path('', views.home, name='home')
    ]
    ```
  
  * in the `urls.py` file of a project: match the url for each app:
  
    ```python
    urlpatterns = [
        path("admin/", admin.site.urls),
        # match '' to 'myapp' application
        path('', include('myapp.urls'))
    ]
    ```

### Templates

* Templates need to be put in `templates` folder(The name matters).

* concepts:

  * block:

    ```html
    <title>
            {% block title %}
                Django App
            {% endblock %}
    </title>
    ```

  * extends from the base: to have a consistent style for all the different pages.

    ```html
    {% extends "base.html" %}
    {% block title %} Home Page
    {% endblock %}
    {% block content %}
        <p>This is the home page.</p>
    {% endblock %}

* Use the `render` function to render the template file.

  * template files must be inside the `template` directory.

    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def home(request):
        return render(request, 'home.html')
    
    ```

    


### Database

* ORM: object relational mapping.

* Create a model in `model.py`:

  ```python
  from django.db import models
  
  # Create your models here.
  class ToDoItems(models.Model):
      title = models.CharField(max_length=200)
      completed = models.BooleanField(default=False)
  ```

* Register models in the `admin.py`:

  ```python
  from django.contrib import admin
  from .models import ToDoItems
  
  # Register your models here.
  admin.site.register(ToDoItems)
  ```

* Make migrations: 

  > Any time you make a change to your database models, you need to make migration. Migration is some automatic code that Django will apply to the database, which allows you to change your models and update them while maintaining the data and ensure that if data already exists in the database, you're not gonna break that or remove that when u make changes to the database schema.

  ```bash
  (Django) PS D:\program learning\Django\codes\DjangoDemo> python .\manage.py makemigrations
  Migrations for 'myapp':
    myapp\migrations\0001_initial.py
      - Create model ToDoItems
  (Django) PS D:\program learning\Django\codes\DjangoDemo> python .\manage.py migrate
  ```

### 

