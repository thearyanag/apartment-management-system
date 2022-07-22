from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Visitor

# Create your views here.

def IndexView(request):
    if request.method == 'GET':
        return render(request, 'visitors/index.html')
    if request.method == 'POST':
        visitor_name,phone,identity,address,flat,remarks = request.POST.get('visitor_name'),request.POST.get('phone'),request.POST.get('identity'),request.POST.get('address'),request.POST.get('flat'),request.POST.get('remarks')
        visitor = Visitor(name=visitor_name,phone=phone,identity=identity,address=address,flat=flat,remarks=remarks)
        visitor.save()