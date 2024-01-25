from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        pswd = request.POST['password']
        cpswd = request.POST['cpassword']
        if pswd == cpswd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=pswd)
                user.save()
                messages.info(request, "user created")
                return redirect('login')
        else:
            messages.info(request, "password not matched")
            return redirect('/')
        return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username=username,password=pswd)
        if user is not None:
            auth.login(request,user)
            return render(request,'log_success.html')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')