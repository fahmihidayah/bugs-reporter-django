from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Issue, IssueRepository
from .forms import IssueForm, IssueNoProjectForm,AllIssueForm
from .tables import IssueTable
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_tables2 import SingleTableView

class IssueListView(LoginRequiredMixin, SingleTableView):
    model = Issue
    table_class = IssueTable
    paginate_by = 10
    repository = IssueRepository()

    def get_queryset(self):
        return self.repository.find_by_user(self.request.user)

class IssueCreateFromProjectView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueNoProjectForm
    success_url = reverse_lazy("project_app_project_list")
    issue_repository = IssueRepository()

    def form_valid(self, form : IssueNoProjectForm):
        self.issue_repository.create_issue(form.save(commit=False), self.kwargs['pk'], self.request.user)
        return HttpResponseRedirect(self.success_url)


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm





class IssueDetailView(DetailView):
    model = Issue


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm

