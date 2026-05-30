from django.db import models

class Status(models.Model):
    username = models.CharField(default='', max_length=9999)
    purchasedGames = models.JSONField(default=list)
    purchaseId = models.CharField(default='', max_length=9999)
    
    def __str__(self):
        return self.username

class Game(models.Model):
    name = models.CharField(default='', max_length=9999)
    short_description = models.CharField(default='', max_length=9999)
    version = models.CharField(default='', max_length=9999)
    tags = models.JSONField(default=list)
    discription = models.TextField(default='', max_length=9999)
    attrs = models.JSONField(default=list)
    price = models.IntegerField(default=0)
    image = models.ImageField(default="")
    download_link = models.TextField(default="")
    def __str__(self):
        return self.name

