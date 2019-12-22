from . import models

from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
        )


