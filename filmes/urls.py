from django.urls import path
from filmes import views

app_name = 'filmes'

urlpatterns = [
    path('list/', views.FilmList.as_view(), name='list')
]
