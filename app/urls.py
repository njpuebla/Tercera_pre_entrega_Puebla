from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio),
    path('electricas/', views.Electrica, name="Electricas"),
    path('acusticas/', views.Acustica, name="Acusticas"),
    path('amplificadores/', views.Amplificadore, name="Amplificadores"),
    path('efectos/', views.Efecto, name="Efectos"),
]
