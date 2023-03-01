from django.db import models

# Create your models here.

class Hobby(models.Model):

    def __str__(self):
        return "{} : {}\n".format(self.hobby_name, self.hobby_desc)
    
    hobby_name = models.CharField(max_length=50)
    hobby_desc = models.CharField(max_length=50)
    hobby_image = models.CharField(max_length=500, default="https://static.vecteezy.com/system/resources/previews/005/068/699/original/a-simple-gear-logo-or-icon-design-vector.jpg")


class Portfolio_item(models.Model):
    
    def __str__(self):
        return "{} : {}\n".format(self.portfolio_item_name, self.portfolio_item_desc)

    portfolio_item_name = models.CharField(max_length=50)
    portfolio_item_desc = models.CharField(max_length=50)
    portfolio_image = models.CharField(max_length=500, default="https://static.vecteezy.com/system/resources/previews/005/068/699/original/a-simple-gear-logo-or-icon-design-vector.jpg")

class Contact_Info(models.Model):

    def __str__(self):
        return self.contact_name

    contact_name = models.CharField(max_length=32)
    contact_email = models.CharField(max_length=64)
    contact_message = models.CharField(max_length=256)