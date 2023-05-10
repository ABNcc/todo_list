from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg", 'id': "task_input", 'type': "text", 'placeholder': "Task",
               'aria-label': "task input", 'autofocus': ""}), error_messages={'required': "Task is required", 'max_length': "Task must be 50 characters or less"})

    description = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'id': "description_input", 'type': "text", 'placeholder': "Description (optional)",
               'aria-label': "description input"}), required=False, error_messages={'max_length': "Description must be 100 characters or less"})


class Noteform(forms.Form):
    note = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'type': "text", 'placeholder': "Note",
                                                         'aria-label': "note input", 'autofocus': ""}), error_messages={'required': "Note is required"})


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
