from django.urls import path

from . import views

app_name = 'animals'
urlpatterns = [
   # ex: /animals/
    path('', views.index, name='index'),
    # ex: /animals/results/
    path('<int:animal_id>/results/', views.results, name='results'),
    # ex: /polls/vote/
    path('vote/', views.vote, name='vote'),
]
