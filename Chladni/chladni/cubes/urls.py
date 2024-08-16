# cubes/urls.py
from django.urls import path

from cubes.views import index


urlpatterns = [
    path('Chladni/chladni/cubes/templates', index),
]