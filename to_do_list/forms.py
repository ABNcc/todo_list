from django import forms


class TaskForm(forms.Form):
    task = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': "form-control form-control-lg", 'type': "text", 'placeholder': "Task",
               'aria-label': "task input"}))

    description = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': "text", 'placeholder': "Description",
               'aria-label': "description input"}), required=False)


class Noteform(forms.Form):
    note = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control form-control-lg", 'type': "text", 'placeholder': "Note",
                                                         'aria-label': "note input"}))
