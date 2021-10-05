"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from to_do_list.views import delete_note, note_view, task_view, add_task, delete_task, completed_task_view, note_view, add_note, delete_note

urlpatterns = [
    path('', task_view, name='Task'),
    path('add/', add_task, name='add'),
    path('completed/<int:task_id>', completed_task_view, name='completed'),
    path('delete/<int:task_id>', delete_task, name='delete'),
    path('note/', note_view, name='note'),
    path('add_note/', add_note, name='add note'),
    path('delete_note/<int:note_id>', delete_note, name='delete note'),
    path('admin/', admin.site.urls),
]

handler404 = 'to_do_list.views.error_404'
