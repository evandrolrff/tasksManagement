from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks_list', views.tasks_list, name='tasks_list'),
]