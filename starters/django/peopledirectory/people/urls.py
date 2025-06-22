from django.urls import path
from .views import people_directory

urlpatterns = [
    path('', people_directory, name='people_directory'),
] 