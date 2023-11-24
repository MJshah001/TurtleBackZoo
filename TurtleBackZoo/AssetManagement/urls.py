from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_home,name='asset_home'),
]
