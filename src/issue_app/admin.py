from django.contrib import admin
from django import forms
from .models import Issue

class IssueAdminForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = '__all__'


class IssueAdmin(admin.ModelAdmin):
    form = IssueAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'description', 'type', 'priority', 'status']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'description', 'type', 'priority', 'status']

admin.site.register(Issue, IssueAdmin)


