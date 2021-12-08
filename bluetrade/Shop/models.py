from django.db import models
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.postgres.fields import ArrayField

# Create your models here.
# For the Arrayfield like User.commoditylist and Photo.url, a splitted string is used to represent a list
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, null=False)
    email = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    phone = models.CharField(max_length=28, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    avatarurl = models.CharField(max_length=128)
    likecommoditylist = models.CharField(max_length=4096, blank=True)

    class Meta:
        verbose_name_plural = "Users"

    def __unicode__(self):
        return self.name


class CommodityType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    description = models.TextField(blank=True)


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    commodityid = models.CharField(max_length=128, null=False)
    name = models.CharField(max_length=64, null=False)
    # owner = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    url = models.CharField(max_length=1024, default="")
    category = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    subcategory = models.CharField(max_length=64, blank=True)
    numofstock = models.IntegerField(default=0)
    onsale = models.BooleanField(default=True)
    createdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)

    selectedbuyer = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Commodities"
        #ordering = ('-addtime',)#

    def __unicode__(self):
        return self.name


class Message(models.Model):
    # the bid message from buyer left for the seller
    id = models.AutoField(primary_key=True)
    price = models.FloatField(blank=False)
    message = models.TextField(blank=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=False)

    class Meta:
        verbose_name_plural = "Messages"

    def __unicode__(self):
        return self.id


class Bid(models.Model):
    # the bid information for the deal
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    price = models.CharField(max_length=48, null=False)
    isCompleted = models.BooleanField(default=False)


class CompletedOrder(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    completeDate = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    # concatenate the urls into one string with space to split, in the form of "www.google.com www.facebook.com"
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=1024, null=False)
    commodityid = models.CharField(max_length=128)


class Avatar(models.Model):
    # the user avatar
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=256, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str({"name": self.name, "owner": self.owner, "type":self.type, "description": self.description, "price": self.price})

