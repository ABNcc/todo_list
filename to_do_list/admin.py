from django.contrib import admin
from .models import ToDoList, Note
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Note)