from django import forms
from .models import Project, UserProject

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class AddUserForm(forms.Form):

    email = forms.EmailField(label='User Email')
    user_type = forms.ChoiceField(choices=((1, "Tester"),(2, "Employee")))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("email"),
            Field("user_type"),
            Submit("add", "Add", css_class="btn-primary"),
        )


