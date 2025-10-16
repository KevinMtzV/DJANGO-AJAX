from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Incluye las URLs de la app core
    path('', include('core.urls')), 
]