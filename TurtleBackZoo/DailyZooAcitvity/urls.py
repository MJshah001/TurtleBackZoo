from django.urls import path
from . import views

urlpatterns = [
    path('', views.dailyzooacitvity_home,name='dailyzooacitvity_home'),
    path('dailyzooacitvity_home/', views.dailyzooacitvity_home,name='dailyzooacitvity_home'),
    path('asset_management',views.asset_management,name='asset_management'),
    path('daily_zoo_activity',views.daily_zoo_activity,name='daily_zoo_activity'),
    path('management_and_reporting',views.management_and_reporting,name='management_and_reporting')
    
]
