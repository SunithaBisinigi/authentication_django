from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo

def home(request):
    context = {
        'message': 'Hello, Django! welcome to home page',
    }
    return render(request, 'home.html', context)
def mem(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers,
    }
    return render(request, 'all_members.html', context)
def landing(request):
    context = {
        'message': 'Hello, Django! Landing page',
    }
    return render(request, 'landing.html', context)
# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('user')
#         password = request.POST.get('pass1')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, "Bad credentials")
#             return redirect('landing')
#     context = {
#         'message': 'Hello, welcome to signin page',
#     }
#     return render(request, 'signin.html', context)
# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['pass1']
#         if User.objects.filter(username=username).exists():
#             return redirect("signup")
#         user = User.objects.UserInfo(username, email, password)
#         user.first_name = fname
#         user.last_name = lname
#         user.save()
#         messages.success(request, "Your account has been successfully created")
#         return redirect("signin")
#     context = {
#         'message': 'Hello, welcome to signup page',
#     }
#     return render(request, 'signup.html', context)
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserInfo

# ...

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        
        if User.objects.filter(username=username).exists():
            return redirect("signup")
        
        # Create a new User instance
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        
        # Create a new UserInfo instance and associate it with the User
        userinfo = UserInfo(user=user,username=username, first_name=fname, last_name=lname, email=email, password=password)
        userinfo.save()
        
        messages.success(request, "Your account has been successfully created")
        return redirect("signin")
    
    context = {
        'message': 'Hello, welcome to signup page',
    }
    return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass1')
        
        # Try to authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if a corresponding UserInfo record exists
            try:
                userinfo = UserInfo.objects.get(user=user)
                login(request, user)
                return redirect('home')
            except UserInfo.DoesNotExist:
                messages.error(request, "Bad credentials")
                return redirect('landing')
        
        else:
            messages.error(request, "Bad credentials")
            return redirect('landing')
    
    context = {
        'message': 'Hello, welcome to signin page',
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('landing')
