from django.contrib import admin
from curso.models import Curso

class Cursos(admin.ModelAdmin):
  list_display = ('id', 'codigo_curso','nome')
  list_display_links = ('id', 'codigo_curso','nome')
  search_fields = ('nome', 'codigo_curso', 'level')
  list_per_page = 20


admin.site.register(Curso,Cursos)



# Register your models here.
