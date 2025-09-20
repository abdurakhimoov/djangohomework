from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Create_profile(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)

    def __str__(self):
        return self.name