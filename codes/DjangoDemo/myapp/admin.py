from django.contrib import admin
from .models import ToDoItems

# admin account:
# username: admin
# password: django123

# Register your models here.
admin.site.register(ToDoItems)
