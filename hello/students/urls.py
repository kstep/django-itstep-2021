import rest_framework.routers
from django.urls import path, re_path, register_converter, include

from . import views


class YearConverter:
    regex = r'[12][0-9]{3}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '{:04}'.format(value)


register_converter(YearConverter, 'y')


router = rest_framework.routers.DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('ex', views.show_students_view),
    path('',
         views.ShowStudentsView.as_view(),
         name='student-list'),
    path('<int:pk>', views.ShowStudentView.as_view(),
         name='student-detail'),

    path('<y:year>', views.ShowStudentView.as_view()),

    path('new', views.CreateStudentView.as_view(),
         name='student-create'),
    path('<int:pk>/edit', views.EditStudentView.as_view(),
         name='student-update'),
]