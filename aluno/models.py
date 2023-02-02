from django.db import models

class Aluno(models.Model):
  nome=models.CharField(max_length=50)
  rg=models.CharField(max_length=9)
  cpf=models.CharField(max_length=11)
  data_nascimento=models.DateField()
  
  def __str__(self) -> str:
    return F'cpf: {self.nome} - nome: {self.cpf}'