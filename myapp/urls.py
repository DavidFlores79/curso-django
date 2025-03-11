from django.urls import path
from . import views

# Cada app tiene sus propias rutas
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('tasks', views.tasks, name="tasks"),
    path('tasks/create', views.create_task, name="create_task"),
    path('projects/create', views.create_project, name="create_project"),
]
