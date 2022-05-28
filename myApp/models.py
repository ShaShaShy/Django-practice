from django.db import models

# Create your models here.


class Users(models.Model):
	firstName = models.CharField(max_length = 40)
	middleName = models.CharField(max_length = 40)
	lastName = models.CharField(max_length = 40)
	address = models.CharField(max_length = 40)
	password = models.CharField(max_length = 20)


		