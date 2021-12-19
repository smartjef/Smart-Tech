from django.urls import path
from . import views

urlpatterns=[
    path('',views.eschool_index, name="eschool_index"),
    path('lab/',views.lab, name="lab"),
    path('mine/',views.ManageCourseListView.as_view(),name='manage_course_list'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('create/',views.CourseCreateView.as_view(),name='course_create'),
    path('<pk>/edit/',views.CourseUpdateView.as_view(),name='course_edit'),
    path('<pk>/delete/',views.CourseDeleteView.as_view(),name='course_delete'),
    path('<pk>/module/',views.CourseModuleUpdateView.as_view(),name='course_module_update'),
    path('subject/<subject>/',views.CourseListView.as_view(),name='course_list_subject'),
    path('<slug>/',views.CourseDetailView.as_view(),name='course_detail'),
    path('module/<module_id>/content/<model_name>/create/',views.ContentCreateUpdateView.as_view(),name='module_content_create'),
    path('module/<module_id>/content/<model_name>/<id>/',views.ContentCreateUpdateView.as_view(),name='module_content_update'),
    path('content/<id>/delete/',views.ContentDeleteView.as_view(),name='module_content_delete'),
    path('module/<module_id>/',views.ModuleContentListView.as_view(),name='module_content_list'),
    path('module/order/',views.ModuleOrderView.as_view(),name='module_order'),
    path('content/order/',views.ContentOrderView.as_view(),name='content_order'),
]