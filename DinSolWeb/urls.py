"""DinSolWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from DinSolAdm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio, name='Inicio'),
    path('Registrar_Usuario/', views.Registrar_Usuario, name='Registrar_Usuario'),
    path('Iniciar_Sesion/', views.Iniciar_Sesion, name='Iniciar_Sesion'),
    path('Cerrar_Sesion/', views.Cerrar_Sesion, name='Cerrar_Sesion'),
    path('Ciiu/', include('Ciiu.urls')),
    # path('Ciiu/Listar/', views.Listar_Ciiu, name='Listar_Ciiu'),
]
