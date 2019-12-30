from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'issue', api.IssueViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Issue
    path('issue/', views.IssueListView.as_view(), name='issue_app_issue_list'),
    path('issue/create/', views.IssueCreateView.as_view(), name='issue_app_issue_create'),
    path('issue/create/<int:pk>', views.IssueCreateFromProjectView.as_view(), name='issue_app_issue_create_from_project'),
    path('issue/detail/<slug:slug>/', views.IssueDetailView.as_view(), name='issue_app_issue_detail'),
    path('issue/update/<slug:slug>/', views.IssueUpdateView.as_view(), name='issue_app_issue_update'),
)

