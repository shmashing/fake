from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='home'),
  url(r'^add/$', views.add_cat, name='add'),
  url(r'^add_cat/$', views.make_cat, name='addCat'),
  url(r'^(?P<id>\d+)/$', views.show_cat, name='showCat'),
  url(r'^(?P<id>\d+)/edit$', views.edit, name='edit'),
  url(r'^(?P<id>\d+)/update$', views.update_cat, name='update'),
  url(r'^(?P<id>\d+)/remove$', views.remove_cat, name='remove'),  
  url(r'^(?P<id>\d+)/add_like$', views.add_like, name='addLike'),
  url(r'^(?P<id>\d+)/remove_like$', views.remove_like, name='removeLike'),
]
