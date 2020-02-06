from django.contrib import admin
from django import forms
from .models import Comment

class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['text', 'created', 'last_updated']
    readonly_fields = ['text', 'created', 'last_updated']

admin.site.register(Comment, CommentAdmin)


