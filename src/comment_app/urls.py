from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'comment', api.CommentViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for comment
    path('comment/', views.CommentListView.as_view(), name='comment_app_comment_list'),
    path('comment/create/', views.CommentCreateView.as_view(), name='comment_app_comment_create'),
    path('comment/detail/<int:pk>/', views.CommentDetailView.as_view(), name='comment_app_comment_detail'),
    path('comment/update/<int:pk>/', views.CommentUpdateView.as_view(), name='comment_app_comment_update'),
    path('comment/create/<int:pk>', views.CommentCreateView.as_view(), name='comment_app_comment_create_with_issue_app'),
)

