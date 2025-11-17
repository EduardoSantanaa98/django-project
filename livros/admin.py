from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao')
    search_fields = ('titulo', 'autor')
    list_filter = ('ano_publicacao',)

# Register your models here.
