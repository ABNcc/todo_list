# Imports
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoList, Note
from .forms import TaskForm, Noteform
from django.views.decorators.http import require_POST
from datetime import datetime


def task_view(request):
    tasks = ToDoList.objects.all()
    form = TaskForm()
    # Inputs
    task_input = request.POST.get('task', form['task'])
    description_input = request.POST.get('description', form['description'])

    return render(request, 'index.html',
                  {'tasks': tasks, 'form': form, 'task_input': task_input, 'description_input': description_input})


@csrf_exempt
@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    # Check if the data for Task entered is valid or not.
    if form.is_valid():
        new_task = ToDoList(
            task=request.POST['task'], description=request.POST['description'])
        new_task.save()
    else:
        return redirect('/error/not_valid_data/')
    return redirect('Task')


@csrf_exempt
@require_POST
def delete_task(request, task_id):
    # Check if the Task wanted to be deleted exists or not so it doesn't show an error
    if ToDoList.objects.filter(pk=task_id).exists():
        ToDoList.objects.get(pk=task_id).delete()
    else:
        return redirect('Task')
    return redirect('Task')


@csrf_exempt
@require_POST
def completed_task_view(request, task_id):
    complete = ToDoList.objects.get(pk=task_id)
    complete.completed = True
    complete.save()
    return redirect('Task')


def error_404(request, exception):
    return render(request, 'not_found.html')


def note_view(request):
    note = Note.objects.all()
    form = Noteform()
    return render(request, 'note.html', {'note': note, 'form': form})


@csrf_exempt
@require_POST
def add_note(request):
    form = Noteform(request.POST)
    # Checks if the entered data for Note valid or not.
    if form.is_valid():
        new_note = Note(note=request.POST['note'], publish_date=datetime.now())
        new_note.save()
    else:
        return redirect('note')
    return redirect('note')


@csrf_exempt
@require_POST
def delete_note(request, note_id):
    # Check if the Note wanted to be deleted exists or not so it doesn't show an error
    if Note.objects.filter(pk=note_id).exists():
        Note.objects.get(pk=note_id).delete()
    else:
        return redirect('note')
    return redirect('note')
