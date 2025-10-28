from django.shortcuts import render
from django.views.generic import ListView
from .models import Filme

# Create your views here.

class FilmList(ListView):
   model = Filme
   template_name = 'filmes/filmes_list.html'
   context_object_name = 'filmes'