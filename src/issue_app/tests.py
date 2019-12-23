import unittest
from django.urls import reverse
from django.test import Client
from .models import Issue
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_issue(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["type"] = "type"
    defaults["priority"] = "priority"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    return Issue.objects.create(**defaults)


class IssueViewTest(unittest.TestCase):
    '''
    Tests for Issue
    '''
    def setUp(self):
        self.client = Client()

    def test_list_issue(self):
        url = reverse('issue_app_issue_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_issue(self):
        url = reverse('issue_app_issue_create')
        data = {
            "name": "name",
            "description": "description",
            "type": "type",
            "priority": "priority",
            "status": "status",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_issue(self):
        issue = create_issue()
        url = reverse('issue_app_issue_detail', args=[issue.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_issue(self):
        issue = create_issue()
        data = {
            "name": "name",
            "description": "description",
            "type": "type",
            "priority": "priority",
            "status": "status",
        }
        url = reverse('issue_app_issue_update', args=[issue.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


