from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView
from voluntary.models import Activity, Organization, Suscription


# Create your views here.


class ListOrganization(ListView):
    model = Organization
    template_name = 'voluntary/detail.html'


class ListActivities(DetailView):
    model = Organization
    template_name = 'voluntary/list_activities.html'


class IndexView(TemplateView):
    template_name = 'voluntary/index.html'


class CreateOrg(CreateView):
    model = Organization
    fields = '__all__'


class CreateAcvitity(CreateView):
    model = Activity
    fields = '__all__'


class CreateSuscription(CreateView):
    model = Suscription
    fields = '__all__'
