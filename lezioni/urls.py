from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_lezioni, name='lista_lezioni'),
    path('<int:lezione_id>/', views.dettaglio_lezione, name='dettaglio_lezione'),
]
