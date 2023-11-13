from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_mensagem, name='exibir_mensagem'),
]
