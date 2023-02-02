from django.contrib import admin
from aluno.models import Aluno 

class Alunos (admin.ModelAdmin):
  list_display = ('id', 'nome','cpf', 'data_nascimento')
  list_display_links = ('id', 'nome')
  search_fields = ('nome', 'cpf',)
  list_per_page = 20
  
admin.site.register(Aluno,Alunos)
# Register your models here.
