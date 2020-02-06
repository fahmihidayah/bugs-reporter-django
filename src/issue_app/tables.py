from django_tables2 import Table, TemplateColumn
from . import models

class IssueTable(Table):

    delete = TemplateColumn(template_name='table/delete.html')

    detail = TemplateColumn(template_name='table/detail.html')

    edit = TemplateColumn(template_name='table/edit.html')

    class Meta:
        model = models.Issue
        fields = ['id', 'project.name', 'name', 'created', 'last_updated', 'type_text', 'priority_text', 'status_text', 'creator_issue.name']
        template_name = 'django_tables2/bootstrap.html'


class IssueViewOnlyTable(Table):

    detail = TemplateColumn(template_name='table/detail.html')
    change_status = TemplateColumn(template_name='issue_app/table/change_status.html')

    class Meta:
        model = models.Issue

        fields = ['id', 'project.name', 'name', 'type_text', 'priority_text', 'status_text', 'creator_issue.name', 'created', 'last_updated', ]
        template_name = 'django_tables2/bootstrap.html'