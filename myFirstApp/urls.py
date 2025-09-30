from django.urls import path
from . import views

urlpatterns = [
    path('myFirstApp/', views.apprenants, name='etudiants'),
    # pour l'url de details d'un etudiant
    path('myFirstApp/details/<int:id>/', views.details, name='details'),
]