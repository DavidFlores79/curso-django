from django.urls import path
from . import views

# Cada app tiene sus propias rutas
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('projects', views.projects),
    path('tasks', views.tasks),
    path('tasks/create', views.create_tasks),
]
