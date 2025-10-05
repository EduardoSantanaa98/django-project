from django.db import models


class Aluno(models.Model):
  nome = models.CharField(max_length=50)
  curso = models.CharField(max_length=50)
  IRA = models.DecimalField(max_digits=4, decimal_places=2)
  data_nascimento = models.DateField()

  def __str__(self):
    return self.nome

class Professor(models.Model):
  nome = models.CharField(max_length=50)
  curso = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  data_nascimento = models.DateField()
  disciplinas = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nome

# Create your models here.
