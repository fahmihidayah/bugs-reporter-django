from django_tables2 import Table, TemplateColumn
from . import models


class ProjectTable(Table):

    delete = TemplateColumn(template_name='table/delete.html')

    detail = TemplateColumn(template_name='table/detail.html')

    edit = TemplateColumn(template_name='table/edit.html')

    create_issue = TemplateColumn(template_name='project_app/table/create_issue.html')

    class Meta:
        model = models.Project
        fields = ['id', 'name', 'created', 'last_updated']
        template_name = 'django_tables2/bootstrap.html'


class UserTable(Table):

    class Meta:
        model = models.UserProject
        fields = ['user.id', 'user.name', 'user.email', 'user_type']
        template_name = 'django_tables2/bootstrap.html'
