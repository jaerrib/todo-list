from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ToDo


class HomePageView(TemplateView):
    template_name = "home.html"


class ToDoListView(ListView):
    model = ToDo
    template_name = "todo_list.html"


class ToDoDetailView(DetailView):
    model = ToDo
    template_name = "todo_detail.html"


class ToDoCreateView(CreateView):
    model = ToDo
    template_name = "todo_new.html"
    fields = ["title", "details", "important", "urgent", "due_date", "creator"]


class ToDoUpdateView(UpdateView):
    model = ToDo
    template_name = "todo_edit.html"
    fields = [
        "title",
        "details",
        "important",
        "urgent",
        "due_date",
    ]


class TodoDeleteView(DeleteView):
    model = ToDo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("todo_list")
