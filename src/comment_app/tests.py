import unittest
from django.urls import reverse
from django.test import Client
from .models import Comment
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


def create_comment(**kwargs):
    defaults = {}
    defaults["text"] = "text"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Comment.objects.create(**defaults)


class commentViewTest(unittest.TestCase):
    '''
    Tests for comment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_comment(self):
        url = reverse('comment_app_comment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        url = reverse('comment_app_comment_create')
        data = {
            "text": "text",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_comment(self):
        comment = create_comment()
        url = reverse('comment_app_comment_detail', args=[comment.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_comment(self):
        comment = create_comment()
        data = {
            "text": "text",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('comment_app_comment_update', args=[comment.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


