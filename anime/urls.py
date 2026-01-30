from django.urls import path
from . import views

urlpatterns = [
    path('anime/list', views.show, name='animes'),
    path('anime/list/add', views.add, name='animes'),
    path('anime/list/find', views.find, name='animes'),
    path('anime/list/update', views.update, name='animes'),
    path('anime/list/delete', views.delete, name='animes'),
]
