from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Request succeeded!")

def february(request):
    return HttpResponse("February")