from django.urls import path
from . import views
from .views import *

app_name = 'client'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('account/registration', RegisterView.as_view(), name='registr'),
    path('logout', views.Logout, name='logout'),
]