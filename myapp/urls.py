from django.urls import include, path
from . import views

urlpatterns = (
    path('', views.contact),
    path('car/', views.car_detail, name='car'),
    path('carlist/', views.car_list_view, name='car-list'),
    path('register/', views.register, name='register'),

)
