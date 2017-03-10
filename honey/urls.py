from django.conf.urls import url
from . import views

# Create your views here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^id(?P<pk>[0-9]+)/$', views.id, name='id'),
    url(r'^musician/$', views.musician, name='musician',),    
    url(r'^404/$', views.er404, name='er404',),
    url(r'^messages/$', views.messages, name='messages',),
    url(r'^friends/$', views.friends, name='friends',),
    url(r'^communities/$', views.communities, name='communities',),
    url(r'^gallery/$', views.gallery, name='gallery',),    
    url(r'^gallery2/$', views.gallery2, name='gallery2',),    
]