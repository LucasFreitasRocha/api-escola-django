from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from aluno.views import AlunosViewSet
from curso.views import CursosViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
