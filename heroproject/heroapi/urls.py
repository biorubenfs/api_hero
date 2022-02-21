from django.urls import path, include
from heroapi import views
from rest_framework import routers

urlpatterns = [
    path('heroapi/', views.heroes_list),
    path('heroapi/<int:pk>/', views.hero_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]