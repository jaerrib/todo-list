from django.contrib import admin

from .models import ToDo, ToDoList

admin.site.register(ToDo)
admin.site.register(ToDoList)
