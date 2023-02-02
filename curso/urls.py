
from django.urls import path
from curso.views import cursos

urlpatterns = [
    path('cursos/', cursos, name='curso'),
]
