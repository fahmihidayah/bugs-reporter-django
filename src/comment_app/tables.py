from django_tables2 import Table, TemplateColumn
from . import models

class CommentTable(Table):

    class Meta:
        model = models.Comment
        fields = ['id', 'text', 'created', 'last_updated']
        template_name = 'django_tables2/bootstrap.html'
