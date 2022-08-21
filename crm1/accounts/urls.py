from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accounts-dashboard'),
    path('user/', views.userPage, name="accounts-user-page"),
    path('login/', views.loginPage, name='accounts-login-user'),
    path('logout/', views.logoutUser, name='accounts-logout-user'),
    path('register/', views.registerPage, name='accounts-register-user'),
    path('products/', views.products, name='accounts-products'),
    path('customer/<str:pk>/', views.customer, name='accounts-customer-info-page'),
    path('create-order/<str:pk>/', views.createOrder, name='accounts-create-order'),
    path('update-order/<str:pk>/', views.updateOrder, name='accounts-update-order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name="accounts-delete-order"),
]
