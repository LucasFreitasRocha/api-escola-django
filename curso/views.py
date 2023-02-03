from rest_framework import viewsets
from curso.models import Curso
from curso.serializer import CursoSerializer

class CursosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os cursos."""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
