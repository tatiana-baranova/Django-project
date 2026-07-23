from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to my blog")

def contact(request):
    return HttpResponse("This is the contact page of my blog.")