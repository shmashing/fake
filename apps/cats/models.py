from __future__ import unicode_literals
from django.db import models
import re
from ..users.models import User

NAME_REGEX = re.compile(r'[a-zA-Z0-9.,-]*$')

# Create your models here.
class CatManager(models.Manager):
  def makeCat(self, name, age, user_id):
    cat_validation = {
      'isValid':True,
      'errors': [],
      'cat': None,
    }

    if(not NAME_REGEX.match(name) or name == ''):
      cat_validation['isValid'] = False
      cat_validation['errors'].append('Please enter a valid cat name')
  
    try:
      age = int(age)
  
    except:
      cat_validation['isValid'] = False
      cat_validation['errors'].append('Please enter a number for cats age')
  
    if(cat_validation['isValid']):
      cat = Cat.objects.create(name=name, age=age, user=User.objects.get(id=user_id))
  
    return cat_validation

  def updateCat(self, id, name, age):
    cat_validation = {
      'isValid':True,
      'errors': [],
      'cat': None,
    }

    if(not NAME_REGEX.match(name)):
      cat_validation['isValid'] = False
      cat_validation['errors'].append('Please enter a valid cat name')
  
    try:
      age = int(age)
  
    except:
      if(age == ''):
        pass

      else:
        cat_validation['isValid'] = False
        cat_validation['errors'].append('Please enter a number for cats age')
  
    if(cat_validation['isValid']):
      cat = Cat.objects.get(id=id)
      if(name != ''):
        cat.name = name

      if(age != ''):
        cat.age = age

      cat.save()
  
    return cat_validation

    

  def remove(self, cat_id):
    Cat.objects.get(id=cat_id).delete()


  def addLike(self, cat_id, user_id):
    like = Like.objects.create(cat=Cat.objects.get(id=cat_id), user=User.objects.get(id=user_id))

  def removeLike(self, cat_id, user_id):
    Like.objects.filter(cat_id=cat_id).get(user_id=user_id).delete()

class Cat(models.Model):

  name=models.CharField(max_length=100)
  age=models.IntegerField()
  user=models.ForeignKey(User)
  objects=CatManager()
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

  def getLikes(self):
    print('in getUserLikes')
    likes = Like.objects.filter(cat_id=self.id)

    user_ids = []

    for like in likes:
      user_ids.append(like.user.id)

    return user_ids

class Like(models.Model):

  cat=models.ForeignKey(Cat)
  user=models.ForeignKey(User)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_at=models.DateTimeField(auto_now=True)

