from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def listar_livros(request):
    livros = Livro.objects.all().order_by('titulo')
    return render(request, 'livros/listar_livros.html', {'livros': livros})

def adicionar_livro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        autor = request.POST.get('autor', '').strip()
        ano = request.POST.get('ano_publicacao', '').strip()
        if titulo and autor and ano:
            Livro.objects.create(titulo=titulo, autor=autor, ano_publicacao=int(ano))
            return redirect('listar_livros')
    return render(request, 'livros/adicionar_livro.html')

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo', livro.titulo).strip()
        livro.autor = request.POST.get('autor', livro.autor).strip()
        ano = request.POST.get('ano_publicacao', livro.ano_publicacao)
        livro.ano_publicacao = int(ano)
        livro.save()
        return redirect('listar_livros')
    return render(request, 'livros/editar_livro.html', {'livro': livro})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request, 'livros/excluir_livro.html', {'livro': livro})
      
    
      

# Create your views here.
