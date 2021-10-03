from django.urls import path, re_path
from . import views
from .views import *

app_name = 'exel'
 
urlpatterns = [
    path('', views.main, name='main'),
    path('prepare/calculate/<int:pk>/', views.calculate, name='calculate'),
    path('cleared/<name_rk>/', views.cleared, name='but_cleared'),
    path('cleared/utm/<name_rk>/', views.utm, name='utm'),
    path('cleared/materials/<name_rk>/', views.materials, name='materials'),
    path('cleared/complete/<name_rk>/', views.complete, name='complete'),
    path('not_cleared/<name_rk>/', views.not_cleared, name='but_not_cleared'),
    path('download/', Download_calc.as_view(), name='download_calc'),
    path('prepare/', Prepare_calc.as_view(), name='prepare'),
    path('buying/', Buying.as_view(), name='buying'),
    path('account/login/', Login.as_view(), name='login'),
    path('account/register/', RegisterView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]

