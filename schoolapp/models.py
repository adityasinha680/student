from django.db import models

# Create your models here.
class Details(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField(max_length=200)
	password=models.CharField(max_length=100)