from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.db import IntegrityError

# Create your views here.


def signup_view(request):

    context = {
        'form': UserCreationForm
    }

    if request.method == 'GET':
        return render(request, 'users/signup.html', context)

    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            user.save()
            login(request, user)
            return redirect('mcp:home')
        except IntegrityError:
            context['error'] = 'Username already exists'
            return render(request, 'users/signup.html', context)
        except Exception as e:
            context['error'] = str(e)
            return render(request, 'users/signup.html', context)

    context['error'] = 'Passwords do not match'
    return render(request, 'users/signup.html', context)


def signin_view(request):

    context = {
        'form': AuthenticationForm
    }

    if request.method == 'GET':
        return render(request, 'users/signin.html', context)

    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )

    if user is not None:
        login(request, user)
        return redirect('mcp:home')
    else:
        context['error'] = 'Invalid credentials'
        return render(request, 'users/signin.html', context)


def signout_view(request):
    logout(request)
    return redirect('mcp:home')
