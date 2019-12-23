from . import models

from rest_framework import serializers


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Issue
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
            'type', 
            'priority', 
            'status', 
        )


