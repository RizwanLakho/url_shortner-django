from django.urls import path 
from home import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('shorten/', views.index_form, name='index_form'),
]
