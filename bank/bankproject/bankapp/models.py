from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class District(models.Model):
    districtname = models.CharField(max_length=100)
    wiki_url = models.URLField(max_length=300)

    def __str__(self):
        return "{}:{}..".format(self.id, self.districtname)


class Branch(models.Model):
    distid = models.ForeignKey(District, on_delete=CASCADE)
    branchname = models.CharField(max_length=100)

    def __str__(self):
        return "{}:{}..".format(self.id, self.branchname)

class Account(models.Model):
    firstname  = models.TextField()
    lastname = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    age = models.IntegerField()
    gender = models.TextField()
    address = models.TextField()
    address2 = models.TextField()
    district = models.TextField()
    branch = models.TextField()
    account = models.TextField()
    material = models.TextField()

    def __str__(self):
        return "{}:{}..".format(self.firstname, self.district)


