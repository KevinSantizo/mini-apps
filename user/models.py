from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	tel = models.IntegerField()
	password = models.CharField(max_length=32)
	birthdate = models.DateField()
	USER_GENDER = (('F', 'Female'), ('M', 'Male'))
	gender = models.CharField(max_length=1, choices=USER_GENDER, default='M')

	def get_absolute_url(self):
		return reverse('voluntary:list_activities', kwargs={'pk': self.pk})

	def __str__(self):
		return self.first_name + self.last_name
