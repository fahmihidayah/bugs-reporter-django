from django import forms
from .models import Issue, User, find_user


from project_app import models as project_models

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse


class AllIssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'status', 'creator_issue', 'project']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'project', 'status']


class IssueNoProjectForm(forms.ModelForm):
    type = forms.ChoiceField(choices=((0, "Bugs"), (1, "Others")))
    priority = forms.ChoiceField(choices=((0, "Major"), (1, "Minor")))
    status = forms.ChoiceField(choices=((0, "Open"), (1, "Closed")))

    def __init__(self, *args, **kwargs):
        super(IssueNoProjectForm, self).__init__(*args, **kwargs)

    def populate_choice(self, user_data):
        if isinstance(self.fields['target_user'], forms.ModelChoiceField):
            target_users: forms.ModelChoiceField = self.fields['target_user']
            target_users.queryset = user_data

    class Meta:
        model = Issue
        fields = ['name', 'description', 'type', 'priority', 'target_user', 'status',]


class IssueEditForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = []

class CommentForm(forms.Form):
    comment = forms.CharField(label='Comment')


class FilterIssue(forms.Form):
    projects = forms.ModelChoiceField(queryset=project_models.ProjectRepository().find_all(), required=False)
    keyword = forms.CharField(label='Keyword', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'user' in self.initial:
            self.fields['projects'].queryset = project_models.ProjectRepository().find_by_own_user(self.initial['user'])

        self.fields['keyword'].required = False
        self.helper = FormHelper()
