from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def Home(request):
#     return HttpResponse("Hey I am django server");

# def Home(request):
#      return HttpResponse("<h1>Hey I am django server</h1>");

# def Home(request):
#     return render(request,"index.html");

def Home(request):
    return render(request,"home/index.html");

def sucess_page(request):
     return HttpResponse("<h1>Hey I am django server</h1>");
