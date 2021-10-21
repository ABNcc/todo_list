# Imports
from typing import Reversible
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoList, Note
from .forms import TaskForm, Noteform, RegisterForm
from django.views.decorators.http import require_POST
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


@csrf_exempt
@login_required
def task_view(request):
    tasks = ToDoList.objects.filter(user=request.user).all()
    form = TaskForm()
    # Inputs
    task_input = request.POST.get('task', form['task'])
    description_input = request.POST.get('description', form['description'])

    return render(request, 'index.html',
                  {'tasks': tasks, 'form': form, 'task_input': task_input, 'description_input': description_input})


@csrf_exempt
@login_required
@require_POST
def add_task(request):
    user = request.user
    form = TaskForm(request.POST)
    # Check if the data for Task entered is valid or not.
    if form.is_valid():
        new_task = ToDoList(user=user,
                            task=request.POST['task'], description=request.POST['description'])
        new_task.save()
    else:
        return redirect('/error/not_valid_data/')
    return redirect('Task')


@csrf_exempt
@login_required
@require_POST
def delete_task(request, task_id):
    user = request.user
    # Check if the Task wanted to be deleted exists or not so it doesn't show an error
    if ToDoList.objects.filter(user=user, pk=task_id).exists():
        ToDoList.objects.get(user=user, pk=task_id).delete()
    else:
        return redirect('Task')
    return redirect('Task')


@csrf_exempt
@login_required
@require_POST
def completed_task_view(request, task_id):
    complete = ToDoList.objects.get(user=request.user, pk=task_id)
    complete.completed = True
    complete.save()
    return redirect('Task')


def error_404(request, exception):
    return render(request, 'not_found.html')


@login_required
@csrf_exempt
def note_view(request):
    note = Note.objects.filter(user=request.user).all()
    form = Noteform()
    return render(request, 'note.html', {'note': note, 'form': form})


@csrf_exempt
@login_required
@require_POST
def add_note(request):
    form = Noteform(request.POST)
    # Checks if the entered data for Note valid or not.
    if form.is_valid():
        new_note = Note(user=request.user,
                        note=request.POST['note'], publish_date=datetime.now())
        new_note.save()
    else:
        return redirect('note')
    return redirect('note')


@csrf_exempt
@login_required
@require_POST
def delete_note(request, note_id):
    user = request.user
    # Check if the Note wanted to be deleted exists or not so it doesn't show an error
    if Note.objects.filter(user=user, pk=note_id).exists():
        Note.objects.get(user=user, pk=note_id).delete()
    else:
        return redirect('note')
    return redirect('note')


@csrf_exempt
def register(request):
    form = RegisterForm(request.POST)
    email_exists = "Email is already used"
    if request.method == "POST":
        if form.is_valid():
            if User.objects.filter(email=request.POST['email']).exists():
                return render(request, "registration/register.html", {'email_exists': email_exists, 'form': form, 'error': form.errors})
            else:
                form.save()
                user = authenticate(
                    username=request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return redirect("Task")

        elif User.objects.filter(email=request.POST['email']).exists():
            return render(request, "registration/register.html", {'error': form.errors, 'email_exists': email_exists, 'form': form})
        else:
            return render(request, "registration/register.html", {'error': RegisterForm(request.POST).errors, 'form': form})
    return render(request, "registration/register.html", {'form': form})
