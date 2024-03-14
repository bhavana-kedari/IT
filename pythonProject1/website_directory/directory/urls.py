# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/<int:category_id>/', views.add_page, name='add_page'),  # Ensure this line is present
]
