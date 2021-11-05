from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="task_user", default="User")
    task = models.CharField(max_length=50, error_messages={
                            'required': "Task field is required"})
    description = models.CharField(max_length=100, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="note_user", default="User")
    note = models.TextField()
    publish_date = models.DateTimeField(blank=True, default=datetime.now())

    def __str__(self):
        return self.note
