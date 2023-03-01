from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Hobby, Portfolio_item
from django.template import loader
from .forms import ContactForm, AddPortfolioItem, EditPortfolioItem

# Create your views here.


def home(request):
    return render(request, 'home/index.html')

def hobbies(request):
    hobbies_list = Hobby.objects.all()
    context = {
        'hobbies_list': hobbies_list,
    }
    return render(request, 'hobbies/hobbies.html',context)

def portfolio(request):
    portfolio_items  = Portfolio_item.objects.all()
    context = {
        'portfolio_items': portfolio_items,
    }
    return render(request, 'portfolio/portfolio.html',context)

def contact(request):
    return render(request, 'home/contact.html')
    ##return HttpResponse("Daniel Hacking\n\nEmail: danielhacking@mail.weber.edu\nPhone: 801-999-9999")

def hobby_page(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobbies/item.html', context)

def portfolio_page(request, portfolio_id):
    portfolio = Portfolio_item.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio/item.html', context)

def contact_form(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
    else:
        form = ContactForm()
    return render(request, 'home/contact_form.html', {'form': form})

def add_portfolio_item(request):
    
    form = AddPortfolioItem(request.POST or None)

    if form.is_valid():
        form.save()
        return render(request, 'portfolio/portfolio.html')
    return render(request, 'portfolio/portfolio_item_form.html', {'form': form})

def edit_portfolio_item(request, portfolio_id):
    item = Portfolio_item.objects.get(id=portfolio_id)
    form = EditPortfolioItem(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('portfolio')
        
    return render(request, 'portfolio/portfolio_item_form.html', {'form': form, 'item': item})

def remove_portfolio_item(request, portfolio_id):
    item = Portfolio_item.objects.get(id=portfolio_id)
    if request.method == 'POST':
        item.delete()
        return redirect('portfolio')
        
    return render(request, 'portfolio/remove_item.html', {'item': item})
