from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_feedback, name='send_feedback')
]