from django.urls import path
from heroapi import views

urlpatterns = [
    path('heroapi/', views.heroes_list),
    path('heroapi/<int:pk>/', views.hero_detail),
]