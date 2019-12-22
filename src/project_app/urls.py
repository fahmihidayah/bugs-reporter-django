from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'project', api.ProjectViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Project
    path('project/', views.ProjectListView.as_view(), name='project_app_project_list'),
    path('project/create/', views.ProjectCreateView.as_view(), name='project_app_project_create'),
    path('project/detail/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_app_project_detail'),
    path('project/delete/<slug:slug>/', views.ProjectDeleteView.as_view(), name='project_app_project_delete'),
    path('project/update/<slug:slug>/', views.ProjectUpdateView.as_view(), name='project_app_project_update'),
    path('project/add_user/<slug:slug>/', views.AddUserToProjectView.as_view(), name='project_app_add_user_to_project'),
    path('project/test_template/<int:pk>', views.TestQueryView.as_view(), name='project_app_test_template'),
)

