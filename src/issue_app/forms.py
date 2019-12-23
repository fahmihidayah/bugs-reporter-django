from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'application' 'status']


class IssueNoApplicationForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'status']

