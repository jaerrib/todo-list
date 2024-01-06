from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ToDo


class HomePageView(TemplateView):
    template_name = "home.html"


class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = "todo_list.html"


class ToDoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ToDo
    template_name = "todo_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    template_name = "todo_new.html"
    fields = ["title", "details", "important", "urgent", "due_date"]

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDo
    template_name = "todo_edit.html"
    fields = [
        "title",
        "details",
        "important",
        "urgent",
        "due_date",
    ]
    success_url = "todo_list"

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("todo_list")

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class ToDoCompleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDo
    template_name = "todo_complete.html"
    fields = [
        "completed",
    ]

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user
