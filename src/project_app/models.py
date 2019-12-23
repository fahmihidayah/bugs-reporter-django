from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()

TYPE_USER_OWNER = 0
TYPE_USER_TESTER = 1
TYPE_USER_EMPLOYER = 2

USER_TYPE = ['Owner', 'Tester', 'Employee']


class UserProject(models.Model):
    user = models.ForeignKey(User, related_name='user_project_user', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', related_name='user_project_project', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=TYPE_USER_OWNER)

    def user_type(self):
        return USER_TYPE[self.status]


class Project(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=255)

    users = models.ManyToManyField(
        User, through=UserProject, related_name='user_project'
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('project_app_project_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('project_app_project_update', args=(self.slug,))


    def get_delete_url(self):
        return reverse('project_app_project_delete', args=(self.slug,))


class UserProjectRepository(object):

    def create_with_email(self, email, project_slug, type):
        user = User.objects.filter(models.Q(email=email)).first()
        if user:
            project: Project = Project.objects.get(slug=project_slug)
            return self.create(user, project, type)
        else:
            return None


    def find_by_project_user(self, project, user):
        return UserProject.objects.filter(models.Q(project=project) & models.Q(user=user))

    def create(self, user, project, type):
        query_contain = self.find_by_project_user(project, user)
        print("contain {}".format(query_contain.count()))
        if query_contain.count() == 0:
            return UserProject.objects.create(user=user, project=project, status=type)
        else:
            user_project = query_contain.first()
            user_project.status = type
            user_project.save()
            return user_project

    def find_by_project_slug(self, slug):
        return UserProject.objects.filter(models.Q(project__slug=slug))

class ProjectRepository(object):

    def find_by_pk(self, pk, user) -> Project:
        return Project.objects.filter(models.Q(slug=pk)).first()

    def find_by_slug_and_count_user_status_owner(self, slug, user):
        return Project.objects \
            .filter(models.Q(slug=slug)) \
            .annotate(count_users=models.Count('users',
                                               filter=models.Q(users__pk=user.id)
                                                      &
                                                      models.Q(user_project_project__status=TYPE_USER_OWNER)))\
            .first()

    def find_by_own_user(self, user):
        # return Project.objects.filter(models.Q(users=user)).filter(models.Q(users__user_project_user__status="1"))
        return Project\
            .objects\
            .filter(models.Q(users__id=user.id) & models.Q(user_project_project__status=TYPE_USER_OWNER))\


    def find_user_project_by_project(self, project):
        return UserProject.objects.filter(project=project)

    def find_user_by_project(self, project):
        return User.objects.filter(models.Q(user_project=project))
        #.filter(models.Q(users__user_project_user__status="1"))