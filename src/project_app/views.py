from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView

from .models import Project, UserProject, ProjectRepository, User, UserProjectRepository, TYPE_USER_OWNER
from .forms import ProjectForm, AddUserForm
from .tables import ProjectTable, UserTable
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from guardian.mixins import PermissionRequiredMixin


class ProjectListView(LoginRequiredMixin, SingleTableView):
    model = Project
    paginate_by = 10
    table_class = ProjectTable
    repository: ProjectRepository = ProjectRepository()

    def get_queryset(self):
        return self.repository.find_by_own_user(self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("project_app_project_list")
    repository : UserProjectRepository = UserProjectRepository()

    def form_valid(self, form : ProjectForm):
        self.repository.create(user=self.request.user, project=form.save())
        return HttpResponseRedirect(self.success_url)


class ProjectDetailView(PermissionRequiredMixin, LoginRequiredMixin, SingleTableView):
    permission_required = "project_app.view_project"
    model = UserProject
    paginate_by = 10
    table_class = UserTable
    repository: ProjectRepository = ProjectRepository()
    user_project_repository = UserProjectRepository()
    template_name = "project_app/project_detail.html"

    def get_permission_object(self):
        self.extra_context = {'object': self.repository.find_by_slug_and_count_user_status_owner(self.kwargs['slug'], user=self.request.user)}
        return self.extra_context['object']

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['object'] = self.extra_context['object']
        context['add_user_form'] = AddUserForm()
        return context

    def get_queryset(self):
        return self.user_project_repository.find_by_project_slug(self.kwargs['slug'])


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("project_app_project_list")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("project_app_project_list")


    def get_success_url(self):
        return super(ProjectDeleteView, self).get_success_url()


class AddUserToProjectView(LoginRequiredMixin, TemplateView):
    http_method_names = ['post']
    user_project_repository = UserProjectRepository()

    def post(self, request, *args, **kwargs):
        form : AddUserForm = AddUserForm(data=request.POST)
        if form.is_valid():
            user_project = self.user_project_repository.create_with_email(form.cleaned_data['email'],
                                                           self.kwargs['slug'],
                                                           form.cleaned_data['user_type'])
            if user_project:
                pass
            else:
                pass

        return HttpResponseRedirect("/project/detail/{}".format(self.kwargs['slug']))


class TestQueryView(TemplateView, LoginRequiredMixin):
    template_name = "project_app/test_template.html"
    repository = ProjectRepository()

    def get_context_data(self, **kwargs):
        context = super(TestQueryView, self).get_context_data(**kwargs)
        pk = kwargs['pk']
        project = self.repository.find_by_pk(pk, self.request.user)
        context['object'] = self.repository.find_by_slug_and_count_user_status_owner(project.slug, self.request.user)
        return context