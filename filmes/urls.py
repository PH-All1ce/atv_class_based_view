from django.urls import path
from filmes import views

app_name = 'filmes'

urlpatterns = [
    path('list/', views.FilmList.as_view(), name='list'),
    path('<int:pk>/details/', views.FilmDetail.as_view(), name='detail'),
    path('create/', views.FilmCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.FilmUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.FilmDelete.as_view(), name='delete')
]