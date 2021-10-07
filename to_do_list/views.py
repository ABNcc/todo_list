from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoList, Note
from .forms import TaskForm, Noteform
from django.views.decorators.http import require_POST
from datetime import datetime


def task_view(request):
    tasks = ToDoList.objects.all()
    form = TaskForm()
    task_input = request.POST.get('task', form['task'])
    description_input = request.POST.get('description', form['description'])

    return render(request, 'index.html',
                  {'tasks': tasks, 'form': form, 'task_input': task_input, 'description_input': description_input})


@csrf_exempt
@require_POST
def add_task(request):
    # task = request.POST['task']   1
    # description = request.POST['description']   2
    form = TaskForm(request.POST)
    if form.is_valid():
        # new_task = ToDoList.objects.create(task=task, description=description) # can be used with (1 and 2) but the one below takes one line instead of 3 lines
        new_task = ToDoList(
            task=request.POST['task'], description=request.POST['description'])
        new_task.save()
    else:
        return redirect('/error/not_valid_data/')
    return redirect('Task')


@csrf_exempt
# @require_POST # Here I used the common thing(405 error) but in the -completed_task_view- I used my way
def delete_task(request, task_id):
    if request.method == 'POST':
        if ToDoList.objects.filter(pk=task_id):
            ToDoList.objects.get(pk=task_id).delete()
        else:
            return redirect('Task')
    else:
        return redirect('/error/did_you_just...?')
    return redirect('Task')


@csrf_exempt
# @require_POST #(I used the -are you kidding me- url instead beacause it dosen't show the task id and it's more funny😃😃)
def completed_task_view(request, task_id):
    if request.method == 'POST':
        complete = ToDoList.objects.get(pk=task_id)
        complete.completed = True
        complete.save()
    else:
        return redirect('/error/are_you_kidding_me/')
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
    if form.is_valid():
        new_note = Note(note=request.POST['note'], publish_date=datetime.now())
        new_note.save()
    else:
        return redirect('note')
    return redirect('note')


@csrf_exempt
@require_POST
def delete_note(request, note_id):
    if Note.objects.filter(pk=note_id):
        Note.objects.get(pk=note_id).delete()
    else:
        return redirect('note')
    return redirect('note')
