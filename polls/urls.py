from django.urls import path
from . import views
app_name = 'polls'
urlpatterns =[
    path('',views.IndexView.as_view(), name="polls_index"),
    path('<int:pk>/', views.DetailView.as_view(), name="polls_detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="polls_results"),
    path('<int:question_id>/vote/',views.vote, name="polls_vote"),
    path('create poll/', views.create, name="polls_create"),
]