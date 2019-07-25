from django.db import models
from django.urls import reverse
from user.models import User

# Create your models here.


class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    org_tel = models.IntegerField()

    def get_absolute_url(self):
        return reverse('voluntary:list_activities', kwargs={'pk': self.pk})

    def __str__(self):
        return self.org_name


class Activity(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    act_name = models.CharField(max_length=255)
    TYPE_CHOICES = (
        (1, 'Salud'),
        (2, 'Alimentación'),
        (3, 'Instrucción'),
    )
    type = models.IntegerField(choices=TYPE_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    requeriment = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('voluntary:list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.act_name + ' -----> ' + self.organization.org_name


class Suscription(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_name = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name.first_name + '------->' + self.activity_name.act_name

