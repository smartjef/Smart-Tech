from django.urls import path
from . import views

app_name = "shop"
urlpatterns=[
    path('', views.product_list, name="product_list"),
    path('about/',views.about, name="about"),
    path('join us/',views.JoinTeam.as_view(), name="join"),
    path('application success/',views.app_success, name="teamsuccess"),
    path('<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),
]
