from django.db import models


class  Curso(models.Model):
  NIVEL = {
    ('B', 'basico'),
    ('I', 'intermediario'),
    ('A', 'avancado')
  }
  codigo_curso=models.CharField(max_length=10)
  nome=models.CharField(max_length=50)
  descricao=models.CharField(max_length=100)
  level=models.CharField(max_length=1, blank=False, default='B', choices=NIVEL)
  
  def __str__(self) -> str:
    return self.nome

