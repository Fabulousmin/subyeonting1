from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.MatchingProListView.as_view()),
    path('<int:pk>', views.MatchingProDetailListView.as_view()),
]
