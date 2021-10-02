from django.db import models
from datetime import datetime


class ToDoList(models.Model):
    task = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    
class Note(models.Model):
    note = models.TextField()
    publish_date = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return self.note
