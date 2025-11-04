# Importa views genéricas do Django para listas e detalhes
from django.views.generic import ListView, DetailView

# Importa o modelo Movie que será usado nas views
from .models import Movie


# 🎬 View baseada em classe para listar todos os filmes
class MovieListView(ListView):
    model = Movie  # Modelo que será listado
    template_name = (
        "movies/movie_list.html"
    )  # Caminho do template usado para renderizar
    context_object_name = (
        "movies"  # Nome da variável no template (em vez de 'object_list')
    )


# 🎥 View baseada em classe para exibir detalhes de um filme
class MovieDetailView(DetailView):
    model = Movie  # Modelo a ser detalhado
    template_name = (
        "movies/movie_detail.html"  # Caminho do template de detalhes
    )
    # Nome da variável no template (em vez de 'object')
    context_object_name = "movie"
    slug_field = "slug"  # Campo usado para buscar o objeto na URL
    slug_url_kwarg = "slug"  # Nome do parâmetro na URL


#TODO - DICAS
## Views com Django Genéricas

# O Django fornece views genéricas para acelerar a
# criação de funcionalidades comuns; no caso do app
# `movies`, usamos duas:

### MovieListView

# - Herda de `ListView`
# - Lista todos os filmes do banco de dados
# - Usa o template `movie_list.html`
# - No template, os filmes estão disponíveis na variável `movies`

# ### MovieDetailView

# - Herda de `DetailView`
# - Mostra os detalhes de um único filme
# - Usa o template `movie_detail.html`
# - O filme é recuperado pela slug da URL
# - No template, o filme está disponível na variável `movie`


# TODO 

    # def MovieListView(request):
    #     movies = Movie.objects.all()
    