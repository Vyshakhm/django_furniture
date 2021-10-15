from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_name = request.POST['email']
        username = request.POST['user_name']
        password = request.POST['password']
        password2=request.POST['password1']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email_name).exists():
                messages.info(request,'email already exists')
                return register('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email_name,username=username,password=password)
                user.save()
        else:
            messages.info(request,"password doesn't match")
            return redirect('register')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['user_name']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    return render(request,'login.html',{'msg':messages})


def logout(request):
    auth.logout(request)
    return redirect('/')
