from django.urls import path
from . import views

urlpatterns = [
    path('',views.Agenda,name='agenda'),
    path('contato_salvo',views.Contato_salvo, name="contato_salvo"),
    path('novo',views.Novo,name='novo'),
    path('home',views.Home,name='home'),
    path('pesquisar',views.Pesquisar,name='pesquisar'),
    path('gestao',views.Gestao,name='gestao'),
    path('sobre',views.Sobre,name='novo'),



]
