from django.http import HttpResponse
from django.shortcuts import render
from .models import Hobby, Portfolio_item

# Create your views here.


def home(request):
    return HttpResponse("Welcome! My name is Daniel, and this is a portfolio of my projects and assigments. I've been going to school for a computer science degree for roughly 3 years at this point, and am working on finishing my BA.")

def hobbies(request):
  hobbiesList = Hobby.objects.all()
  return HttpResponse(hobbiesList)

def portfolio(request):
    portfolio  = Portfolio_item.objects.all()
    return HttpResponse(portfolio)

def contact(request):
    return HttpResponse("Daniel Hacking\n\nEmail: danielhacking@mail.weber.edu\nPhone: 801-999-9999")