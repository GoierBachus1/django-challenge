from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    # Capturar filtros de la URL
    search_query = request.GET.get('search', '')
    priority_filter = request.GET.get('priority', '')

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    context = {
        'tasks': tasks,
        'search_query': search_query,
        'priority_filter': priority_filter,
    }
    return render(request, 'tasks_list.html', context)

def task_detail(request, pk):
    task = get_object_or_404(Task,pk=pk)
    return render(request, "task_detail.html", {"task":task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm()
    return render(request, "task_form.html",{"form":form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, "task_form.html",{"form":form, "task":task})

def task_delete(request, pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, "task_confirm_delete.html",{"task":task})
