from django.shortcuts import render
from django.views.generic.edit import CreateView
from user.models import User
# Create your views here.


class CreateUser(CreateView):
    model = User
    fields = '__all__'
