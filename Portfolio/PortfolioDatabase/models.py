from django.db import models

# Create your models here.

class Hobby(models.Model):

    def __str__(self):
        return "{} : {}\n".format(self.hobby_name, self.hobby_desc)
    
    hobby_name = models.CharField(max_length=50)
    hobby_desc = models.CharField(max_length=50)


class Portfolio_item(models.Model):
    
    def __str__(self):
        return "{} : {}\n".format(self.portfolio_item_name, self.portfolio_item_desc)

    portfolio_item_name = models.CharField(max_length=50)
    portfolio_item_desc = models.CharField(max_length=50)

