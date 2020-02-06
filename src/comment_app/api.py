from . import models
from . import serializers
from rest_framework import viewsets, permissions


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for the comment class"""

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


