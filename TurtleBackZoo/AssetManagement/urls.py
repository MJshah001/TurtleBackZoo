from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_management_home,name='assetmanagement_home'),
    path('asset_management',views.asset_management,name='asset_management'),
    path('daily_zoo_activity',views.daily_zoo_activity,name='daily_zoo_activity'),
    path('management_and_reporting',views.management_and_reporting,name='management_and_reporting'),
    path('asset_management', views.asset_management_home,name='assetmanagement_home'),
    
    # building's links
    path('building/', views.building_actions, name='building_actions'),
    path('add_building/', views.add_building, name='add_building'),
    path('edit_building/<str:name>/', views.edit_building, name='edit_building'),
    path('delete_building/<str:name>/', views.delete_building, name='delete_building'),
    
    path('attractions/', views.attraction_actions, name='attraction_actions'),
    path('concession/', views.concession_actions, name='concession_actions'),

    # employees's link
    path('employee/employee/', views.employee_actions, name='employee_actions'),
    path('employee/add_employee/', views.add_employee, name='add_employee'),
    path('info_employee/', views.info_employee, name='info_employee'),
    path('employee/edit_employee/<int:emp_number>/', views.edit_employee, name='edit_employee'),
    path('employee/delete_employee/<int:emp_number>/', views.delete_employee, name='delete_employee'),
    
    # attractions's links
    path('attraction/add_attraction/', views.add_attraction, name='add_attraction'),
    path('attraction/edit_attraction/<str:attraction_name>/', views.edit_attraction, name='edit_attraction'),
    path('attraction/delete_attraction/<str:attraction_name>/', views.delete_attraction, name='delete_attraction'),
    
    # concession's link
    path('asset/concession/', views.concession_actions, name='concession_actions'),
    path('asset/concession/add_concession/', views.add_concession, name='add_concession'),
    path('asset/concession/edit_concession/<str:concession_name>/', views.edit_concession, name='edit_concession'),
    path('asset/concession/delete_concession/<str:concession_name>/', views.delete_concession, name='delete_concession'),
    
    # Animal's Links
    path('animal/', views.animal_actions, name='animal_actions'),
    path('animal/add_animal/', views.add_animal, name='add_animal'),
    path('animal/edit_animal/<int:tag_number>/', views.edit_animal, name='edit_animal'),
    path('animal/delete_animal/<int:tag_number>/', views.delete_animal, name='delete_animal'),
    
    # Enclosure's Links
    path('enclosure/', views.enclosure_actions, name='enclosure_actions'),
    path('enclosure/add_enclosure/', views.add_enclosure, name='add_enclosure'),
    path('enclosure/edit_enclosure/<str:enclosure_number>/', views.edit_enclosure, name='edit_enclosure'),
    path('enclosure/delete_enclosure/<str:enclosure_number>/', views.delete_enclosure, name='delete_enclosure'),
]
