from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^login_fun$', views.login_fun),
    url(r'^logout$', views.logout),   
]