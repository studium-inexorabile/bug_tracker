from django.contrib.auth.models import User

from bug_tracker_api.models import Bug
from bug_tracker_api.serializers import UserSerializer, BugSerializer
from rest_framework import generics, permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BugList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BugDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Bug.objects.all()
    serializer_class = BugSerializer
