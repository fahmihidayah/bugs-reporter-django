from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView, View
from .models import Issue, IssueRepository, find_user
from .forms import IssueForm, IssueNoProjectForm,AllIssueForm, CommentForm, FilterIssue
from .tables import IssueTable, IssueViewOnlyTable
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from project_app import models as project_models
from comment_app import models as comment_models
from comment_app import tables as comment_tables
from comment_app import forms as comment_forms


class IssueListView(LoginRequiredMixin, SingleTableView):
    model = Issue
    table_class = IssueViewOnlyTable
    paginate_by = 10
    repository = IssueRepository()
    project_repository: project_models.ProjectRepository = project_models.ProjectRepository()

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        context['form'] = FilterIssue(initial={'user':self.request.user})
        context['list_projects'] = self.project_repository.find_by_own_user(self.request.user)
        return context

    def get_queryset(self):
        form : FilterIssue = FilterIssue(data=self.request.GET)
        form.is_valid()
        keys = form.cleaned_data
        keys['user'] = self.request.user
        return self.repository.find_by_target_user(keys)


class IssueCreatorListView(LoginRequiredMixin, SingleTableView):
    model = Issue
    table_class = IssueTable
    paginate_by = 10
    repository = IssueRepository()

    def get_queryset(self):
        return self.repository.find_by_creator_user(self.request.user)


class IssueCreateFromProjectView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueNoProjectForm
    success_url = reverse_lazy("project_app_project_list")
    issue_repository = IssueRepository()

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form : IssueNoProjectForm = form_class(**self.get_form_kwargs())
        form.populate_choice(find_user(self.kwargs['pk']))
        return form

    def form_valid(self, form : IssueNoProjectForm):
        self.issue_repository.create_issue(form.save(commit=False), self.kwargs['pk'], self.request.user)
        return HttpResponseRedirect(self.success_url)


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm


class IssueDetailView(LoginRequiredMixin, SingleTableView):
    model = comment_models.Comment
    comment_repository: comment_models.CommentRepository= comment_models.CommentRepository()
    issue_repository: IssueRepository= IssueRepository()
    table_class = comment_tables.CommentTable
    paginate_by = 10
    template_name = "issue_app/issue_detail.html"

    def get_queryset(self):
        return self.comment_repository.find_by_issue_slug(self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(IssueDetailView, self).get_context_data(**kwargs)
        context['form'] = comment_forms.CommentForm()
        context['object'] = self.issue_repository.find_by_slug(self.kwargs['slug'])
        return context

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm


class IssueUpdateDoneView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect('')
