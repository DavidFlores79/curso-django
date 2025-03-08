from django.urls import path
from . import views

# Cada app tiene sus propias rutas
urlpatterns = [
    path('', views.index),
    path('contact/<str:username>', views.about),
    path('projects', views.projects),
    path('tasks', views.tasks),
]
