
from django.urls import path
from aluno.views import alunos

urlpatterns = [
    path('alunos/', alunos, name='aluno'),
]
