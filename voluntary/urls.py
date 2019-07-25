from django.urls import path
from . import views

app_name = 'voluntary'
urlpatterns = [
    path('<int:pk>/', views.ListOrganization.as_view(), name='list_activities'),
    path('<int:pk>/org/', views.ListActivities.as_view(), name='list'),
    path('input_org/', views.CreateOrg.as_view(), name='organization_form'),
    path('input_act/', views.CreateAcvitity.as_view(), name='activity_form'),
    path('input_susc/', views.CreateSuscription.as_view(), name='suscription_activity'),
    path('', views.IndexView.as_view(), name='index'),
]