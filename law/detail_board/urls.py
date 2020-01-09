from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('family_board/', views.family_board, name="family_board"),
]