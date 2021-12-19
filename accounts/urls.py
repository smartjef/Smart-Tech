from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name="index"),
    path('contact',views.ContactView.as_view(), name="contact"),
    path('subscribe',views.SubscribeView.as_view(), name="subscribe"),
    path('profile',views.ProfileView.as_view(), name="profile"),
    path('profile-update',views.ProfileUpdateView.as_view(), name="profile_update"),
    path('shortcuts',views.settings, name="settings"),
    path('about', views.AboutView.as_view(), name="about"),
    path('services', views.ServiceView.as_view(), name="service"),
]