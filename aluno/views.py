from rest_framework import viewsets
from aluno.models import Aluno
from aluno.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos."""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
