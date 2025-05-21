Title: Building a Simple Django To-Do Application

```python
# models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# views.py
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'add_task.html')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]

# templates/task_list.html
<!DOCTYPE html>
<html>
<head>
    <title>Task List</title>
</head>
<body>
    <h1>Tasks</h1>
    <ul>
        {% for task in tasks %}
            <li>
                {{ task.title }} - {% if task.completed %}Done{% else %}Pending{% endif %}
                <a href="{% url 'complete_task' task.id %}">Complete</a>
            </li>
        {% endfor %}
    </ul>
    <a href="{% url 'add_task' %}">Add Task</a>
</body>
</html>

# templates/add_task.html
<!DOCTYPE html>
<html>
<head>
    <title>Add Task</title>
</head>
<body>
    <h1>Add a New Task</h1>
    <form method="post">
        {% csrf_token %}
        <input type="text" name="title" placeholder="Task title" required>
        <button type="submit">Add</button>
    </form>
</body>
</html>
```
