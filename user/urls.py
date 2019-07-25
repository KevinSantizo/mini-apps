from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='user_form'),
]