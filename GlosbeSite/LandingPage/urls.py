from django.conf.urls import include, url
from . import views #Hace un import de todo lo de la carpeta actual aqui

urlpatterns = [
    url(r'^$', views.index),
]