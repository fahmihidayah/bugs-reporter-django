from . import models
from . import serializers
from rest_framework import viewsets, permissions


class IssueViewSet(viewsets.ModelViewSet):
    """ViewSet for the Issue class"""

    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


