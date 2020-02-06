from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Comment
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from issue_app.models import IssueRepository

from django.http import HttpResponseRedirect

class CommentListView(ListView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy("project_app_project_list")
    issue_repository = IssueRepository()

    def form_valid(self, form : CommentForm):
        data : Comment = form.save(commit=False)
        data.user = self.request.user
        data.issue = self.issue_repository.find_by_id(self.kwargs['pk'])
        data.save()
        return HttpResponseRedirect(self.success_url)



class CommentDetailView(DetailView):
    model = Comment


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm



