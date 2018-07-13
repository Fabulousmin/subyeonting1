from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/',views.PostDetailListView.as_view())
]
