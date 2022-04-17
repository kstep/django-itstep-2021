from django.contrib.auth.models import User
from rest_framework.serializers import Serializer, \
    ModelSerializer
from rest_framework import serializers
from . import models


def not_default(value):
    if value == "Describe new task here...":
        raise serializers.ValidationError("Default description prohibited")



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

class TaskSerializer(ModelSerializer):
    #owner = serializers.HyperlinkedRelatedField(
    #    view_name='user-detail',
    #    queryset=User.objects.filter(is_staff=True))
    owner = UserSerializer()
    description = serializers.CharField(max_length=500,
                                        validators=[not_default])
    class Meta:
        model = models.Task
        fields = '__all__'

