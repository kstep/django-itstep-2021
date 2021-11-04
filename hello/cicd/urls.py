from django.urls import path

from . import views

urlpatterns = [
    path('update_server', views.update_server,
         name='update_server')
]