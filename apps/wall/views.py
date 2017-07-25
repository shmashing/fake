from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from ..users.models import User
from .models import Friend
# Create your views here.
#Friend.objects.all().delete()
def index(request):
    if(not check_user_authentication(request)):
      print('failed authentication at index')
      print(request.session['user_logged'])
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=request.session['user_id']),
      'rec_users': User.objects.exclude(id=request.session['user_id']).order_by('-created_at')[:3],
    }

    return render(request, "wall/index.html", context)

def friends(request):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    user = User.objects.get(id=request.session['user_id'])

    context = {
      'user': user,
      'friends': Friend.objects.filter(user=user)
  
    }

    return render(request, 'wall/friends.html', context)

def user_list(request):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    user = User.objects.get(id=request.session['user_id'])

    context = {
      'users': Friend.objects.getAvailUsers(user),
    }

    return render(request, 'wall/users.html', context)


def add_friend(request, id):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    user = User.objects.get(id=request.session['user_id'])
    friend = User.objects.get(id=id)

    Friend.objects.addFriend(user, friend)

    return redirect('wall:userList')

def rem_friend(request, id):
    if(not check_user_authentication(request)):
      return redirect('users:home')

    user = User.objects.get(id=request.session['user_id'])
    friend = User.objects.get(id=id)

    Friend.objects.removeFriend(user, friend)

    return redirect('wall:friends')

def check_user_authentication(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']
        return True
      else:
        return False
    except:
      return False

