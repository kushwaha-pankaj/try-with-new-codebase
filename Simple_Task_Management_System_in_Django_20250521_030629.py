Title: Simple Task Management System in Django

```python
# Import required Django libraries and classes
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from django import forms
from django.core.wsgi import get_wsgi_application

# Define the Task model representing a task in the task management system
class Task(models.Model):
    title = models.CharField(max_length=200)  # Title of the task
    description = models.TextField()  # Detailed description of the task
    completed = models.BooleanField(default=False)  # Completion status

# Create a form for adding and updating tasks using Django's forms module
class TaskForm(forms.ModelForm):
    class Meta:
        # Bind TaskForm with Task model
        model = Task
        # Specify the fields to include in the form
        fields = ['title', 'description', 'completed'] 

# Create a Django view to list all tasks
def task_list(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    return render(request, 'task_list.html', {'tasks': tasks})  # Render task list template with tasks

# Create a view to handle the creation of a new task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm()  # Create an empty form for GET requests
    return render(request, 'add_task.html', {'form': form})  # Render the add task template

# Create a view to handle the updating of an existing task
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Fetch the task by ID
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task to the database
            return redirect('task_list')  # Redirect to the task list
    else:
        form = TaskForm(instance=task)  # Prefill form with existing task data
    return render(request, 'edit_task.html', {'form': form})  # Render the edit task template

# Define URL patterns to map views
urlpatterns = [
    path('', task_list, name='task_list'),  # Home page displaying the task list
    path('add/', add_task, name='add_task'),  # Page to add a new task
    path('edit/<int:task_id>/', edit_task, name='edit_task'),  # Page to edit an existing task
]

# Define minimal Django settings for the app
settings = {
    'DEBUG': True,
    'INSTALLED_APPS': [
        __name__,  # Register the current script as a Django app
    ],
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Use SQLite database
            'NAME': 'db.sqlite3',  # Database name
        }
    },
    'ROOT_URLCONF': __name__,  # Set the current script as root URL configuration
    'SECRET_KEY': 'a-very-secret-key',  # Secret key for the application
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['./templates'],  # Directory containing HTML templates
        }
    ]
}

# Create a WSGI application object for running the app
application = get_wsgi_application()

# Run the Django management utility if executed as the main program
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line()  # Execute Django's command-line utility
```

Make sure to create a `templates` folder with `task_list.html`, `add_task.html`, and `edit_task.html` files, containing the corresponding HTML for displaying and processing the tasks.