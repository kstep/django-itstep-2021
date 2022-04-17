from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='todo-index'),
    path('/settings.js', views.JsSettingsView.as_view(), name='js-settings'),

    path('api/', include(router.urls)),

    #path('api/tasks', views.TaskViewSet.as_view({
    #    'get': 'list',
    #    'post': 'create',
    #}), name='task-resource'),
    #path('api/tasks/<int:id>', views.TaskViewSet.as_view({
    #    'get': 'retrieve',
    #})),
]