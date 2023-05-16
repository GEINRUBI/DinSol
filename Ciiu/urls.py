from django.urls import path
from . import views

urlpatterns = [
    path('Crear/', views.Crear_Ciiu, name='Crear_Ciiu'),
    path('Listar/', views.Listar_Ciiu, name='Listar_Ciiu'),
    path('Lista/<int:Ciius_id>/', views.Ciiu_Creada, name='Ciiu_Creada'),
    path('Elimina/<int:Ciius_id>/Eliminar/', views.Elimina_Ciiu, name='Elimina_Ciiu'),
]
