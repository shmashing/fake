from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.
class FriendManager(models.Manager):
  def addFriend(self, user, friend):
    try:
      Friend.objects.filter(user=user).get(friend=friend)

    except:
      Friend.objects.create(user=user, friend=friend)
      Friend.objects.create(user=friend, friend=user)

  def removeFriend(self, user, friend):
    Friend.objects.filter(user=user).get(friend=friend).delete()
    Friend.objects.filter(user=friend).get(friend=user).delete()

  def getFriends(self, user):
    friends = Friend.objects.filter(user=user)

    friend_ids = []
    for friend in friends:
      friend_ids.append(friend.friend.id)

    return friend_ids

  def getAvailUsers(self, user):
    friends = Friend.objects.getFriends(user)
    users = User.objects.exclude(id=user.id)

    avail_users = []

    for user in users:
      if user.id in friends:
        pass
      else:
        avail_users.append(user)

    return avail_users
    

class Friend(models.Model):
  user = models.ForeignKey(User, related_name='user')
  friend = models.ForeignKey(User, related_name='toFriend')
  objects = FriendManager()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

