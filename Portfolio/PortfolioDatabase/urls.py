from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('contact/', views.contact, name="contact"),
]