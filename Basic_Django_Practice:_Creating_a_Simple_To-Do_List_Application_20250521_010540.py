Title: Basic Django Practice: Creating a Simple To-Do List Application

```python
# Import necessary modules from Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.urls import path
from django.forms import ModelForm

# Define the Task model, which represents a task in the to-do list
class Task(models.Model):
    description = models.CharField(max_length=255)  # Task description
    completed = models.BooleanField(default=False)  # Status of the task, default is not completed

    def __str__(self):
        return self.description

# Create a form class for the Task model to handle task creation and updates
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'completed']  # Fields we want to expose in the form

# Define a view to list all tasks in the to-do list
def task_list_view(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    context = {'tasks': tasks}  # Context dictionary to pass tasks to the template
    return render(request, 'task_list.html', context)  # Render task_list.html with task data

# Define a view to create a new task
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Bind data from request to form
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list view
    else:
        form = TaskForm()  # Create an empty form instance

    return render(request, 'task_form.html', {'form': form})  # Render the form template

# Define a view to update an existing task
def task_update_view(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by its ID
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind request data to form with task instance
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)  # Populate the form with task data

    return render(request, 'task_form.html', {'form': form})  # Render the update form

# Define URL patterns for the application
urlpatterns = [
    path('', task_list_view, name='task_list'),  # URL for listing tasks
    path('task/new/', task_create_view, name='task_new'),  # URL for creating a new task
    path('task/<int:task_id>/edit/', task_update_view, name='task_edit'),  # URL for editing a task
]

# Simulation of Django templates (for illustrative purposes only)

# task_list.html:
"""
{% extends 'base_generic.html' %}

{% block content %}
  <h2>To-Do List</h2>
  <ul>
    {% for task in tasks %}
      <li>
        <a href="{% url 'task_edit' task.id %}">{{ task.description }}</a>
        {% if task.completed %} - Completed{% endif %}
      </li>
    {% endfor %}
  </ul>
  <a href="{% url 'task_new' %}">Add New Task</a>
{% endblock %}
"""

# task_form.html:
"""
{% extends 'base_generic.html' %}

{% block content %}
  <h2>New Task</h2>
  <form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
"""
```

Note: This code provides a basic Django application setup, which includes models, views, and URL mappings. The code is designed to manage a simple to-do list, allowing users to create, view, and update tasks. The templates are represented as strings here, but in a full Django application, they should be stored as separate HTML files in the `templates` directory. The code snippet outlines the core functionalities of a typical Django application while maintaining simplicity and readability.