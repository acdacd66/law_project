from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('family_board/', views.family_board, name="family_board"),
    path('traffic_board/', views.traffic_board, name="traffic_board"),
    path('government_board/', views.government_board, name="government_board"),
    path('army_board/', views.army_board, name="army_board"),
    path('labor_board/', views.labor_board, name="labor_board"),
    path('financial_board/', views.financial_board, name="financial_board"),
    path('trade_board/', views.trade_board, name="trade_board"),
    path('leisure_board/', views.leisure_board, name="leisure_board"),
    path('lawsuit_board/', views.lawsuit_board, name="lawsuit_board"),
    path('welfare_board/', views.welfare_board, name="welfare_board"),
    path('estate_board/', views.estate_board, name="estate_board"),
    path('business_board/', views.business_board, name="business_board"),
    path('crime_board/', views.crime_board, name="crime_board"),
    path('client_board/', views.client_board, name="client_board"),
    path('children_board/', views.children_board, name="children_board"),
    path('information_board/', views.information_board, name="information_board"),
    path('startup_board/', views.startup_board, name="startup_board"),
    path('eco_board/', views.eco_board, name="eco_board"),

    ]