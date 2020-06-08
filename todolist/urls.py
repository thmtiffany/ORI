from django.urls import path

from . import views

urlpatterns = [
path('', views.todolist, name ='todolist'),
path('add', views.addTask, name='add'),
path('complete/<task_id>', views.completeTask, name="complete"),
path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
path('deleteall', views.deleteAll, name='deleteall')
]
