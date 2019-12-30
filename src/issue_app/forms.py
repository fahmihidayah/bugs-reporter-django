from django import forms
from .models import Issue


class AllIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'status', 'creator_issue', 'project']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'project', 'status']


class IssueNoProjectForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'status',]


