from django.shortcuts import render, redirect, reverse
from ..users.models import User
from django.contrib import messages
from .models import Cat, Like
# Create your views here.
def index(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=user_id),
      'cats': Cat.objects.all(),
    }

    return render(request, "cats/index.html", context)

def add_cat(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=user_id),
    }

    return render(request, 'cats/add_cat.html', context)


def show_cat(request, id):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=user_id),
      'cat': Cat.objects.get(id=id),
    }

    return render(request, 'cats/cat_page.html', context)

def make_cat(request):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    cat_name = request.POST['cat_name']
    cat_age = request.POST['cat_age']

    print(cat_name, cat_age)
    cat_validation = Cat.objects.makeCat(cat_name, cat_age, user_id)

    if(cat_validation['isValid']):
      print('cat validation susseful')
      return redirect('cats:home')
    else:
      print('cat validation unsusseful')
      for error in cat_validation['errors']:
        messages.add_message(request, messages.INFO, error)

      return redirect('cats:add')

def edit(request, id):
    try:
      if(request.session['user_logged']):
        if(request.session['user_id'] != Cat.objects.get(id=id).user_id):
          return redirect('cats:home')

        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    context = {
      'user': User.objects.get(id=user_id),
      'cat': Cat.objects.get(id=id),
    }

    return render(request, 'cats/edit.html', context)

def update_cat(request, id):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    cat_name = request.POST['cat_name']
    cat_age = request.POST['cat_age']

    cat_validation=Cat.objects.updateCat(id, cat_name, cat_age)

    if(cat_validation['isValid']):
      return redirect('cats:home')
    else:
      for error in cat_validation['errors']:
        messages.add_message(request, messages.INFO, error)

    return redirect(reverse('cats:edit', kwargs={'id':id}))


def remove_cat(request, id):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    Cat.objects.remove(id)

    return redirect('cats:home')

def add_like(request, id):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    Cat.objects.addLike(id, user_id)    

    return redirect('cats:home')

def remove_like(request, id):
    try:
      if(request.session['user_logged']):
        user_id = request.session['user_id']

      else:
        return redirect('users:home')
    except:
      return redirect('users:home')

    Cat.objects.removeLike(id, user_id)    

    return redirect('cats:home')

