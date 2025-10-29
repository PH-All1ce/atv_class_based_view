from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Filme
from .forms import FilmeForm

# Create your views here.
def home(request):
   return render(request, 'home.html')

class FilmList(ListView):
   model = Filme
   template_name = 'filmes_list.html'
   context_object_name = 'filmes'

class FilmDetail(DetailView):
   model = Filme
   template_name = 'filmes_detail.html'
   context_object_name = 'filmes'

class FilmCreate(CreateView):
   model = Filme
   form_class = FilmeForm
   template_name = 'filmes_form.html'
   success_url = reverse_lazy('filmes:list')

class FilmUpdate(UpdateView):
   model = Filme
   form_class = FilmeForm
   template_name = 'filmes_form.html'
   success_url = reverse_lazy('filmes:list')

class FilmDelete(DeleteView):
   model = Filme
   template_name = 'filmes_delete.html'
   success_url = reverse_lazy('filmes:list')