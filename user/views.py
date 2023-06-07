from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserReg
# Create your views here.


def home(request):
    return render(request, 'Home.html')



def register(request):
    if request.method == 'POST':
        form = UserReg(request.POST)
        if form.is_valid():
            form.save()


            messages.success(request,f'Your account has beeed Created. Now you can login')
            return redirect('login')
    else:
        form = UserReg()

    context = {'form':form}
    return render(request, 'register.html',context)