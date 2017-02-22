from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^id(?P<pk>[0-9]+)/$', views.id, name='id'),
]