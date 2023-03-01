from django import forms
from .models import Contact_Info, Portfolio_item


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Info
        fields = ['contact_name', 'contact_email', 'contact_message']

class AddPortfolioItem(forms.ModelForm):
    class Meta:
        model = Portfolio_item
        fields = ['portfolio_item_name', 'portfolio_item_desc', 'portfolio_image']


class EditPortfolioItem(forms.ModelForm):
    class Meta:
        model = Portfolio_item
        fields = ['portfolio_item_name', 'portfolio_item_desc', 'portfolio_image']
