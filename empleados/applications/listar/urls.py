from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('listar/', views.EmpleadosListView.as_view()),
    path('listarn/', views.NominaListView.as_view()),
    path('creare/', views.EmpleadosCreateView.as_view()),
    path('crearn/', views.NominaCreateView.as_view()),
    path('editare/<pk>/', views.EmpleadosUpdateView.as_view()),
    path('editarn/<pk>/', views.NominaUpdateView.as_view()),
    path('eliminare/<pk>/', views.EmpleadosDeleteView.as_view()),
    path('eliminarn/<pk>/', views.NominaDeleteView.as_view()),
]