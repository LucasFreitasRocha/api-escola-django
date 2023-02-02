from django.http import JsonResponse
from aluno.service import Service
def alunos(request):
  service = Service()
  if request.method == 'GET':
    return JsonResponse(service.list_alunos())

# Create your views here.
