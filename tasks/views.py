from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Information
from .forms import TaskForm


def index(request):
    return render(request, 'tasks/index.html')


def tasks_list(request):
    tasks = Information.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Information, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'tasks/task_edit.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Information, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form': form})
