from django.contrib import admin
from .models import Categoria, Contato


# editar area administrativa e caracteristicas da categoria contatos
class ContatoAdmin(admin.ModelAdmin):
    # deixar os campos visiveis
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    # deixar os campos clicaveis
    list_display_links = ('id', 'nome', 'sobrenome')
    # opcao de filtrar
    # list_filter = ('nome', 'sobrenome')
    # buscar campos
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_per_page = 10
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
