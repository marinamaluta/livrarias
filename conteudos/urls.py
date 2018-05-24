from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tema/<int:x>/', views.tema, name='tema-list'),
    path('tema/<int:x>/<int:tipo>', views.tema_tipo, name='tema-tipo'),
    path('estatisticas', views.estatisticas, name='stats')
]