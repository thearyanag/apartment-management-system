from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Visitor
from .forms import newUserForm

# Create your views here.

def IndexView(request):
    if request.method == 'GET':
        return render(request, 'visitors/index.html')
    if request.method == 'POST':
        visitor_name,phone,identity,address,flat,remarks = request.POST.get('visitor_name'),request.POST.get('phone'),request.POST.get('identity'),request.POST.get('address'),request.POST.get('flat'),request.POST.get('remarks')
        visitor = Visitor(name=visitor_name,phone=phone,identity=identity,address=address,flat=flat,remarks=remarks)
        visitor.save()

def register_request(request):
    if request.method == "POST":
        form = newUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        messages.error(request, 'Invalid credentials')
    form = newUserForm()
    return render(request, 'visitors/register.html', {'register_form': form})    

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You are now logged in as %s' % user.username)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'visitors/login.html', {'login_form': form})