from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hobbies/', views.hobbies, name="hobbies"),
    path('hobbies/<int:hobby_id>', views.hobby_page, name="hobby_page" ),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio/<int:portfolio_id>', views.portfolio_page, name="portfolio_page" ),
    path('portfolio/Add', views.add_portfolio_item, name="add_portfolio_item" ),
    path('portfolio/Edit_<int:portfolio_id>', views.edit_portfolio_item, name="edit_portfolio_item" ),
    path('portfolio/Remove_<int:portfolio_id>', views.remove_portfolio_item, name="remove_portfolio_item" ),
    path('contact/', views.contact, name="contact"),
    path('contact_form/', views.contact_form, name="contact_form"),
]