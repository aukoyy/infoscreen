from django.contrib import admin

# Register your models here.

from .models import TodoModel, TodoList

admin.site.register(TodoModel)
admin.site.register(TodoList)