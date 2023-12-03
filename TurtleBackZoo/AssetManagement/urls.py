from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_management_home,name='assetmanagement_home'),
    path('asset_management',views.asset_management,name='asset_management'),
    path('daily_zoo_activity',views.daily_zoo_activity,name='daily_zoo_activity'),
    path('management_and_reporting',views.management_and_reporting,name='management_and_reporting'),
    path('asset_management', views.asset_management_home,name='assetmanagement_home'),
    path('building/', views.building_actions, name='building_actions'),
    path('add_building/', views.add_building, name='add_building'),
    path('edit_building/<str:name>/', views.edit_building, name='edit_building'),
    path('delete_building/<str:name>/', views.delete_building, name='delete_building'),
    # path('employees/', views.employee_actions, name='employee_actions'),
    path('attractions/', views.attraction_actions, name='attraction_actions'),
    path('concession/', views.concession_actions, name='concession_actions'),
    
    
    
    path('employee/employee/', views.employee_actions, name='employee_actions'),
    path('employee/add_employee/', views.add_employee, name='add_employee'),
    path('info_employee/', views.info_employee, name='info_employee'),
    path('employee/edit_employee/<int:emp_number>/', views.edit_employee, name='edit_employee'),
    path('employee/delete_employee/<int:emp_number>/', views.delete_employee, name='delete_employee'),
]
