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

TYPE_TEXT = {0 : "BUGS", 1 : "OTHER"}
STATUS_TEXT = {0 : "OPEN", 1 : "CLOSED"}
PRIORITY_TEXT = {0 : "MAJOR", 1 : "MINOR"}


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

    project = models.ForeignKey(project_models.Project, related_name='project_issues', on_delete=models.CASCADE, default=None)

    def type_text(self):
        return TYPE_TEXT.get(self.type)

    def priority_text(self):
        return PRIORITY_TEXT[self.priority]

    def status_text(self):
        return STATUS_TEXT[self.status]


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('issue_app_issue_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('issue_app_issue_update', args=(self.slug,))


class IssueRepository(object):

    project_repository = project_models.ProjectRepository()

    def find_by_user(self, user: User):
        return Issue.objects.filter(models.Q(target_user=user))

    def find_by_target_user(self, filter):
        return Issue.objects.filter(models.Q(target_user=filter['user']))
        # if 'projects' not in filter:
        #     return Issue.objects.filter(models.Q(target_user=filter['user']))
        # else:
        #     return Issue.objects.filter(models.Q(target_user=filter['user'])
        #                             & models.Q(project__id=filter['projects'])
        #                             & models.Q(name__icontains=filter['keyword']))

    def find_by_creator_user(self, user: User):
        return Issue.objects.filter(models.Q(creator_issue=user))

    def find_by_slug(self, slug):
        return Issue.objects.filter(models.Q(slug=slug)).first()

    def find_by_id(self, id):
        return Issue.objects.filter(models.Q(pk=id)).first()

    def create_issue(self, issue : Issue, project_id, creator : User):
        issue.project = self.project_repository.find_by_id(project_id)
        issue.creator_issue = creator
        issue.save()
        return issue

def find_user(project_id):
    return project_models.ProjectRepository().find_user_by_project_id(project_id)
