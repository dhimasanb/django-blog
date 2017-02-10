from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.post_home, name='index'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^detail/$', views.post_create, name='detail'),
    url(r'^update/$', views.post_create, name='update'),
    url(r'^delete/$', views.post_create, name='delete'),
]
