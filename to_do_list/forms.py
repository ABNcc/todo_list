from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg", 'type': "text", 'placeholder': "Task",
               'aria-label': "task input", 'autofocus': ""}))

    description = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': "text", 'placeholder': "Description",
               'aria-label': "description input"}), required=False)


class Noteform(forms.Form):
    note = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'type': "text", 'placeholder': "Note",
                                                         'aria-label': "note input", 'autofocus': ""}))


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
