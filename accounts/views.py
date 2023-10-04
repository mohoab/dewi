from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import  CustomUserCreation
from .models import Customeuser



def Login(request):
    if request.user.is_authenticated:
        return redirect('root:home')
    elif request.method == 'GET':
        form=AuthenticationForm()
        context = {
            'form': form ,
        }
        
        return render(request,'registration/login.html',context=context)
    else:
        if '@' in request.POST.get('username'):
            username =Customeuser.objects.get(email=request.POST.get('username')).username
        form=AuthenticationForm(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password1')
        user=authenticate(username=username,password=password)
        if user is not None :
            login(request, user)
            return redirect('root:home')
        else:
            messages.add_message(request,messages.ERROR,'your email or password invalid')
            return redirect(request.path_info)
        

@login_required
def Logout(request):
    logout(request)
    return redirect('root:home')
def Signup(request):
    if request.user.is_authenticated:
        return redirect('root:home')
    elif request.method == 'GET':
        form=CustomUserCreation()
        context = {
            'form': form ,
        }
        
        return render(request,'registration/signup.html',context=context)
    else:
        form=CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST.get('username')
            password=request.POST.get('password1')
            user=authenticate(username=username,password=password)
            if user is not None :
                login(request, user)
                return redirect('root:home')   
            
        else:
            messages.add_message(request,messages.ERROR,'your data is invalid')
            return redirect(request.path_info)

    