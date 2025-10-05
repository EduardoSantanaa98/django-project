import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Aluno, Professor
from .serializers import AlunoSerializer, ProfessorSerializer


class AlunoViewSet(viewsets.ModelViewSet):
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
  queryset = Professor.objects.all()
  serializer_class = ProfessorSerializer


def home(request):
  return HttpResponse("Hello, Django!")

def personalized_hello(request, name):
  return HttpResponse(f"Hello, {name}!")

@csrf_exempt
def post_hello(request):
    if request.method == "POST":
      try:
        data = json.loads(request.body)
        name = data.get("name", "Guest")
        return JsonResponse({"message": f"Hello, {name}!"})
      except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
      return JsonResponse({"error": "Invalid request method"}, status=405)
def autor(request):
  return render(request, 'autor.html')

def index(request):
  return render(request, 'index.html')

def problema(request):
  return render(request, 'problema.html')

def solucao(request):
  return render(request, 'solucao.html')
  