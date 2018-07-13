# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.MatchingListView.as_view()),
]
