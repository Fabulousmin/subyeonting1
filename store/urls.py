# users/urls.py
from django.urls import include, path

from . import views

urlpatterns = [
    path('category/', views.CategroyListView.as_view()),
    path('category/<int:pk>/', views.CategroyDeatailListView.as_view()),

    path('shop/', views.ShopListView.as_view()),
    path('shop/<int:pk>/', views.ShopDetailListView.as_view()),

    path('review/', views.ReviewListView.as_view()),
    path('review/<int:pk>/', views.ReviewDetailListView.as_view()),

    path('item/', views.ItemListView.as_view()),
    path('item/<int:pk>/', views.ItemDetailListView.as_view()),
]
