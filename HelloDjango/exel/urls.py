from django.urls import path, re_path
from . import views
from .views import *

app_name = 'exel'

urlpatterns = [
    path('', Prepare_calc.as_view(), name='prepare'),
    path('calculate/<int:pk>/', views.calculate, name='calculate'),
]

'''
path('', views.main, name='main'),
path('prepare/calculate/<int:pk>/', views.calculate, name='calculate'),
path('cleared/<int:pk>/', views.cleared, name='but_cleared'),
path('cleared/utm/<int:pk>/', views.utm, name='utm'),
path('cleared/materials/<int:pk>/', views.materials, name='materials'),
path('cleared/complete/<int:pk>/', views.complete, name='complete'),
path('not_cleared/<int:pk>/', views.not_cleared, name='but_not_cleared'),
path('download/', Download_calc.as_view(), name='download_calc'),
path('prepare/', Prepare_calc.as_view(), name='prepare'),
path('buying/', Buying.as_view(), name='buying'),
path('buying_priority/', Dmp_buying.as_view(), name='dmp'),
path('account/login/', Login.as_view(), name='login'),
#path('account/register/', RegisterView.as_view(), name='register'),
path('logout/', views.Logout, name='logout'),
'''
