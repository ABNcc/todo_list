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
from to_do_list.views import delete_note, note_view, register, task_view, add_task, delete_task, completed_task_view, note_view, add_note, delete_note, update_task_view, update_task, update_note_view, update_note, google_verification_page
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', task_view, name="Task"),
    path('?add?/?', add_task, name="add"),
    path('?completed?<int:task_id>?', completed_task_view, name="completed"),
    path('?delete?<int:task_id>?', delete_task, name="delete"),
    path('?update_task??<int:task_id>?', update_task_view, name="update view"),
    path('?update??<int:task_id>?', update_task, name="update task"),
    path('note/', note_view, name="note"),
    path('?add_note?/?', add_note, name="add note"),
    path('?delete_note?<int:note_id>?', delete_note, name="delete note"),
    path('?undate_note??<int:note_id>?', update_note_view, name="update note"),
    path('?undate??<int:note_id>?', update_note, name="update"),
    path('login/', LoginView.as_view(), name="login"),
    path('?logout?9/1?1', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', register, name="register"),
    path('admin/', admin.site.urls),
    path('reset/', PasswordResetView.as_view(template_name='registration/reset.html'), name="reset"),
    path('sent/', PasswordResetDoneView.as_view(template_name='registration/reset.html'),
         name="password_reset_done"),
    path('google07960185c082d602.html', google_verification_page),
    path('confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/reset.html'),
         name="password_reset_confirm"),
    path('complete/', PasswordResetCompleteView.as_view(template_name='registration/complete.html'),
         name="password_reset_complete"),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'to_do_list.views.error_404'
handler500 = 'to_do_list.views.error_500'
