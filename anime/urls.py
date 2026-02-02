from django.urls import path
from . import views

urlpatterns = [
    path('list', views.show, name='animes'),
    path('list/add', views.add, name='animes'),
    path('list/find', views.find, name='animes'),
    path('list/update', views.update, name='animes'),
    path('list/delete', views.delete, name='animes'),
]
