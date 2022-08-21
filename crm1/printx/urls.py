from django.urls import path
# from .views import printx_home
from . import views

urlpatterns = [
    path('', views.printx_home, name='load-devices-1')
]
