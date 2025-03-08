from django.urls import path
from . import views

# Cada app tiene sus propias rutas
urlpatterns = [
    path('', views.helloWord),
    path('contact/<str:username>', views.about)
]
