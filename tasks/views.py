from django.shortcuts import render
from django.http import HttpResponse
from .models import Information

def index(request):
    return HttpResponse("Hello. You're at tasks index.")

def tasks_list(request):
    tasks = Information.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})