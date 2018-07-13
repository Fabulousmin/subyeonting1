from django.urls import include, path

from . import views

urlpatterns = [
    path('users/', views.UserInfoListView.as_view()),
    path('message/', views.MessageListView.as_view()),
]
