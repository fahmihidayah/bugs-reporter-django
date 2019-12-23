from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Issue
from .forms import IssueForm


class IssueListView(ListView):
    model = Issue


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm


class IssueDetailView(DetailView):
    model = Issue


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm

