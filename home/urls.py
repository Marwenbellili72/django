from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('articles/', views.articles),
    path('contactez-nous/', views.contact),
    path('services/', views.services),
    path('login/', views.login),
    path('signup/', views.signup),
]
