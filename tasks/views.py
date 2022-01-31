from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Information

def index(request):
    return HttpResponse("Hello. You're at tasks index.")

def tasks_list(request):
    tasks = Information.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Information, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})