from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework.authentication import SessionAuthentication
from rest_framework.renderers import JSONRenderer, AdminRenderer, BrowsableAPIRenderer
from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle, AnonRateThrottle, BaseThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from todo import models
from todo.serializers import TaskSerializer, UserSerializer


class IndexView(TemplateView):
    template_name = 'todo/index.html'


class JsSettingsView(TemplateView):
    template_name = 'todo/settings.js'


class UserViewSet(ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [
        BrowsableAPIRenderer,
        JSONRenderer,
        AdminRenderer,
    ]


class MyThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return request.user and request.user.is_staff


class TaskViewSet(ModelViewSet):
    throttle_scope = 'tasks'
    throttle_classes = [MyThrottle]
    serializer_class = TaskSerializer
    queryset = models.Task.objects.all().order_by('created_date')

