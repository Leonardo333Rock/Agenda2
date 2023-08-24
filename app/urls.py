from django.urls import path
from . import views

urlpatterns = [
    path('',views.Agenda,name='agenda'),
    path('contato_salvo',views.Contato_salvo, name="contato_salvo")
]
