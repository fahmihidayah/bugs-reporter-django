from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import PositiveIntegerField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

from django.contrib.auth import get_user_model

from project_app import models as project_models

User = get_user_model()


class Issue(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=255)
    type = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    creator_issue = models.ForeignKey(
        User, related_name='created_issues', on_delete=models.CASCADE,
        default=None
    )

    target_user = models.ForeignKey(
        User, related_name='user_issues', on_delete=models.CASCADE,
        default=None
    )

    application = models.ForeignKey(project_models.Project, related_name='project_issues', on_delete=models.CASCADE, default=None)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('issue_app_issue_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('issue_app_issue_update', args=(self.slug,))


