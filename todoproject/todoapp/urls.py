from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('submitpage/', views.submitpage),
]