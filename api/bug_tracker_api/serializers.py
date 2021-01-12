from django.contrib.auth.models import User
from rest_framework import serializers

from bug_tracker_api.models import Bug


class UserSerializer(serializers.ModelSerializer):
    bugs = serializers.PrimaryKeyRelatedField(many=True, queryset=Bug.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'bugs']


class BugSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bug
        fields = ['id', 'title', 'description', 'status', 'owner']
