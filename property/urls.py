from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('register/', views.registerPage, name="register"),

    path('', views.home, name='home'),

    path('profile-types/', views.profile_types, name='profile-types'),
    path('create-profile-type/', views.create_profile_type,
         name='create-profile-type'),
    path('update-profile-type/<str:pk>/',
         views.update_property_type, name='update-profile-type'),
    path('delete-profile-type/<str:pk>/',
         views.delete_profile_type, name='delete-profile-type'),

    path('profiles/', views.profiles, name='profiles'),
    path('create-profile/<str:type_pk>/', views.create_profile,
         name='create-profile'),
    path('update-profile/<str:pk>/',
         views.update_profile, name='update-profile'),
    path('delete-profile/<str:pk>/',
         views.delete_profile, name='delete-profile'),

    path('property-types/', views.property_types, name='property-types'),
    path('create-property-type/', views.create_property_type,
         name='create-property-type'),
    path('update-property-type/<str:pk>/',
         views.update_property_type, name='update-property-type'),
    path('delete-property-type/<str:pk>/',
         views.delete_property_type, name='delete-property-type'),

    path('properties/', views.properties, name='properties'),
    path('create-property/', views.create_property,
         name='create-property'),
    path('update-property/<str:pk>/',
         views.update_property, name='update-property'),
    path('delete-property/<str:pk>/',
         views.delete_property, name='delete-property'),

    path('unit-types/', views.unit_types, name='unit-types'),
    path('create-unit-type/', views.create_unit_type,
         name='create-unit-type'),
    path('update-unit-type/<str:pk>/',
         views.update_unit_type, name='update-unit-type'),
    path('delete-unit-type/<str:pk>/',
         views.delete_unit_type, name='delete-unit-type'),
   
   path('units/', views.units, name='units'),
    path('create-unit/', views.create_unit,
         name='create-unit'),
    path('update-unit/<str:pk>/',
         views.update_unit, name='update-unit'),
    path('delete-unit/<str:pk>/',
         views.delete_unit, name="delete-unit"),
   
   path('occupancies/', views.occupancies, name='occupancies'),
    path('create-occupancy/', views.create_occupancy,
         name='create-occupancy'),
    path('update-occupancy/<str:pk>/',
         views.update_occupancy, name='update-occupancy'),
    path('delete-occupancy/<str:pk>/',
         views.delete_occupancy, name="delete-occupancy"),
]
