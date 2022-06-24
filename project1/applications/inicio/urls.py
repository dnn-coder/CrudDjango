from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('inicio/', views.PruebaView.as_view()),
]
