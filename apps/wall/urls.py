from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='home'),
  url(r'^friends/$', views.friends, name='friends'),
  url(r'^user_list/$', views.user_list, name='userList'),
  url(r'^friends/add_friend/(?P<id>\d+)$', views.add_friend, name='addFriend'),
  url(r'^friends/rem_friend/(?P<id>\d+)$', views.rem_friend, name='remFriend'),

]
