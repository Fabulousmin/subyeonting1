from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view()),
    path('<int:pk>/', views.ProfileDetailListView.as_view()),
]
