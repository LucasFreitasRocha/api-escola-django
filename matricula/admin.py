from django.contrib import admin
from matricula.models import Matricula
# Register your models here.
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula, Matriculas)
