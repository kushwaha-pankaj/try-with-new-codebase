```python
# Title: Building a RESTful API with Django and Django REST Framework

# Import the necessary modules
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.db import models

# Define a simple model for demonstration
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# Create a serializer for the model
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description']

# Define a viewset for the serializer
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Set up the router for the API
router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

# Define the URLs for the application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the API URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Complete the setup in the settings.py and admin.py (not shown for brevity, assume it's done)
```

This code provides a clean and straightforward setup for creating a RESTful API using Django and the Django REST Framework. The code begins by defining a simple `Item` model, a `Serializer` for the model, a `ViewSet` to handle CRUD operations, configures the `router` to expose these endpoints, and finally maps these into the `urlpatterns` list.