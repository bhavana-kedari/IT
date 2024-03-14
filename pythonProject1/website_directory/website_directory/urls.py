from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('', include('directory.urls')),  # Include URLs from your app 'directory'
]