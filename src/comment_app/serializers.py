from . import models

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = (
            'pk', 
            'text', 
            'created', 
            'last_updated', 
        )


