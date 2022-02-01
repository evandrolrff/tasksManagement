from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks-list', views.tasks_list, name='tasks-list'),
    path('task-<int:pk>/', views.task_detail, name='task-detail'),
    path('task/new', views.task_new, name='task-new'),
    path('task-<int:pk>/edit', views.task_edit, name='task-edit'),
]