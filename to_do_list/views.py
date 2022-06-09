# Imports
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoList, Note
from .forms import TaskForm, Noteform, RegisterForm
from django.views.decorators.http import require_POST
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime


@csrf_exempt
@login_required
def task_view(request):
    tasks = ToDoList.objects.filter(user=request.user).all()
    form = TaskForm()
    return render(request, 'index.html', {'tasks': tasks, 'form': form})


@csrf_exempt
@login_required
@require_POST
def add_task(request):
    user = request.user
    # Check if the data for Task entered is valid or not.
    form = TaskForm(request.POST or None)
    if form.is_valid():
        new_task = ToDoList(user=user,
                            task=request.POST['task'], description=request.POST['description'])
        new_task.save()
        return redirect("Task")
    return render(request, "index.html", {'form': form, 'tasks': ToDoList.objects.filter(user=request.user).all(), 'task_len': len(request.POST['task'])})


@csrf_exempt
@login_required
@require_POST
def delete_task(request, task_id):
    user = request.user
    # Check if the Task wanted to be deleted exists or not so it doesn't show an error
    if ToDoList.objects.filter(user=user, pk=task_id).exists():
        ToDoList.objects.get(user=user, pk=task_id).delete()
    return redirect('Task')


@csrf_exempt
@login_required
@require_POST
def completed_task_view(request, task_id):
    if ToDoList.objects.filter(user=request.user, pk=task_id).exists():
        complete = ToDoList.objects.get(user=request.user, pk=task_id)
        complete.completed = True
        complete.save()
        return redirect('Task')
    return redirect('Task')


@csrf_exempt
@login_required
def update_task_view(request, task_id):
    user = request.user
    if ToDoList.objects.filter(user=user, pk=task_id).exists():
        task = ToDoList.objects.get(user=user, pk=task_id)
        return render(request, 'update.html', {'order': task})
    return redirect('Task')


@csrf_exempt
@login_required
@require_POST
def update_task(request, task_id):
    user = request.user
    if ToDoList.objects.filter(user=user, pk=task_id).exists() and 0 < len(request.POST['Task']) <= 50 and len(request.POST['Description']) <= 100:
        updated_task = ToDoList(
            user=user, pk=task_id, task=request.POST['Task'], description=request.POST['Description'])
        updated_task.save()
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
        return redirect('note')
    return render(request, 'note.html', {'note': Note.objects.filter(user=request.user).all(), 'form': form})


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
@login_required
def update_note_view(request, note_id):
    user = request.user
    if Note.objects.filter(user=user, pk=note_id).exists():
        note = Note.objects.get(user=user, pk=note_id)
        return render(request, 'update.html', {'order': note})
    return redirect('note')


@csrf_exempt
@login_required
@require_POST
def update_note(request, note_id):
    user = request.user
    if Note.objects.filter(user=user, pk=note_id).exists() and len(request.POST['Note']) > 0:
        updated_note = Note(
            user=user, pk=note_id, note=request.POST['Note'], publish_date=datetime.now())
        updated_note.save()
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


def google_verification_page(request):
    return(request, 'google07960185c082d602.html')
