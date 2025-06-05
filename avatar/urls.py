from django.urls import path
from . import views
urlpatterns = [
    path('', views.personagens, name = 'personagens'),
    path('originais/', views.personagens_sem_traducao, name = 'personagens_originais'),
]