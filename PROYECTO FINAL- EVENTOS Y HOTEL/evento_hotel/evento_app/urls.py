from django.urls import path
from . import views

urlpatterns = [
    path('', views.pantalla_inicio, name='inicio'),
    path('inicio_sesion/', views.pantalla_inicio_sesion, name='inicio_sesion'),
    path('evento/', views.listar_eventos, name='evento'),
    path('registro/', views.registro, name='registro'),
    path('inscribirse_evento/<int:evento_id>/',views.inscribirse_evento, name='inscribirse_evento'),
    path('perfil_info',views.perfil_usuario, name='perfil_info'),
    
    
]

