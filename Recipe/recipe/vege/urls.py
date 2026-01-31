from django.urls import path 
from .import views

urlpatterns = [
path('',views.receipes,name='receipes'),
path('delete-receipe/<id>/', views.delete_receipe),
path('update_receipe/<id>/', views.update_receipe),
   
]