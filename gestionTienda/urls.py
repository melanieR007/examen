from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [

    path('', views.index, name='index')
    path('principal', views.principal, name='principal'),
]