from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pay.initiate_payment,name='pay'),
    path('callback/', views.Pay.callback, name='callback'),
]