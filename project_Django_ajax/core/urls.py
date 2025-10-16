from django.urls import path
from . import views

urlpatterns = [
    # Vista principal (GET)
    path('', views.selects_view, name='selects'), 
    
    # Endpoint AJAX (GET) para cargar los municipios
    path('api/municipios/<int:estado_id>/', views.get_municipios, name='get_municipios'),
]