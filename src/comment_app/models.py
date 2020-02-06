from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from issue_app import models as issue_model
from django_extensions.db import fields as extension_fields


class Comment(models.Model):

    # Fields
    text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="comments",
    )

    issue = models.ForeignKey(issue_model.Issue, related_name='comment_issue', on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('comment_app_comment_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('comment_app_comment_update', args=(self.pk,))


class CommentRepository(object):

    def __init__(self):
        self.comment_model = Comment

    def find_by_issue_slug(self, issue_slug):
        return self.comment_model.objects.filter(models.Q(issue__slug=issue_slug))


