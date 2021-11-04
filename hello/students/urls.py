from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowStudentsView.as_view(),
         name='student-list'),
    path('<int:pk>', views.ShowStudentView.as_view(),
         name='student-detail'),
    path('new', views.CreateStudentView.as_view(),
         name='student-create'),
    path('<int:pk>/edit', views.EditStudentView.as_view(),
         name='student-update'),
]