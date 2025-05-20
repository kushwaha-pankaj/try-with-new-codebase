Title: Django Practice Project - Blog Application

```python
# Import necessary libraries from Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import path
from django.db import models
from django.contrib import admin
from django import forms

# Define a simple data model for the blog
class Post(models.Model):
    # The title of the blog post
    title = models.CharField(max_length=100)
    # The content of the blog post
    content = models.TextField()
    # The publish date of the blog post
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the title of the post to represent it
        return self.title

# Create a form for submitting a new blog post
class PostForm(forms.ModelForm):
    class Meta:
        # Use the Post model and its fields
        model = Post
        fields = ['title', 'content']

# Django view for listing all blog posts
def list_posts(request):
    # Query to fetch all blog posts ordered by their published date
    posts = Post.objects.all().order_by('-published_date')
    # Render the posts in 'blog/list_posts.html'
    return render(request, 'blog/list_posts.html', {'posts': posts})

# Django view for viewing a single blog post
def view_post(request, post_id):
    # Fetch a single post or return a 404 error if not found
    post = get_object_or_404(Post, pk=post_id)
    # Render post in 'blog/view_post.html'
    return render(request, 'blog/view_post.html', {'post': post})

# Django view for adding a new blog post
def add_post(request):
    if request.method == 'POST':
        # Create a new form instance with POST data
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the new post and redirect to the list of posts
            form.save()
            return HttpResponseRedirect('/')
    else:
        # Create an empty form instance if GET request
        form = PostForm()

    # Render the form in 'blog/add_post.html'
    return render(request, 'blog/add_post.html', {'form': form})

# Define URL patterns for the blog application
urlpatterns = [
    path('', list_posts, name='list_posts'),                 # List all posts at the root URL
    path('post/<int:post_id>/', view_post, name='view_post'), # View single post by ID
    path('add/', add_post, name='add_post'),                 # URL for adding a new post
]

# Register the Post model with the Django admin interface
admin.site.register(Post)
```

```html
<!-- blog/list_posts.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Blog Posts</title>
</head>
<body>
<h1>Blog Posts</h1>
<ul>
    <!-- Loop through all posts and display their titles -->
    {% for post in posts %}
        <li><a href="{% url 'view_post' post.id %}">{{ post.title }}</a></li>
    {% empty %}
        <li>No posts yet.</li>
    {% endfor %}
</ul>
<a href="{% url 'add_post' %}">Add New Post</a>
</body>
</html>
```

```html
<!-- blog/view_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ post.title }}</title>
</head>
<body>
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>
<a href="{% url 'list_posts' %}">Back to posts</a>
</body>
</html>
```

```html
<!-- blog/add_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add New Post</title>
</head>
<body>
<h1>Create a New Blog Post</h1>
<form method="post">
    {% csrf_token %}
    <!-- Render the form fields -->
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{% url 'list_posts' %}">Cancel</a>
</body>
</html>
```