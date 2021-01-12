from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from bug_tracker_api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('bugs/', views.BugList.as_view()),
    path('bugs/<int:pk>/', views.BugDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
