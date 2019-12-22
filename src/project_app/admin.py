from django.contrib import admin
from django import forms
from .models import Project

class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'description']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'description']

admin.site.register(Project, ProjectAdmin)


