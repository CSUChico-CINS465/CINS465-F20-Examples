from django.urls import path
from django.contrib.auth import views as auth_views

from . import views #convention

urlpatterns = [
    path('', views.index),
    path('django_login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('django_logout/', views.logout_view),
    path('suggestions/', views.get_suggestions),
    path('comment/<int:sugg_id>/', views.comment),
    path('suggestion/', views.add_suggestion),
]
