import csv

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import (
    ToDoCreateForm,
    ToDoUpdateForm,
    ToDoListCreateForm,
    ToDoListUpdateForm,
)
from .models import ToDo, ToDoList


class HomePageView(TemplateView):
    template_name = "home.html"


class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = "list_manager.html"

    def get_queryset(self):
        return ToDoList.objects.filter(creator=self.request.user.pk)


class ToDoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ToDo
    template_name = "todo_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    form_class = ToDoCreateForm
    template_name = "todo_new.html"
    context_object_name = "todo_list"
    pk_url_kwarg = "todo_list_pk"

    def get_redirect_url(self, param):
        return reverse_lazy("todo_list_detail", kwargs={"param": param})

    def get_queryset(self):
        return ToDoList.objects.filter(pk=self.kwargs["todo_list_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ToDoCreateForm()
        context["todo_list"] = ToDoList.objects.get(pk=self.kwargs["todo_list_pk"])
        return context

    def form_valid(self, form):
        form.instance.todo_list = ToDoList.objects.get(pk=self.kwargs["todo_list_pk"])
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDo
    form_class = ToDoUpdateForm
    template_name = "todo_edit.html"
    success_url = reverse_lazy("todo_list")

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


def todo_complete(request, pk):
    if "_auth_user_id" not in request.session:
        return redirect("/")
    model = ToDo.objects.get(pk=pk)
    if request.session["_auth_user_id"] != str(model.creator.pk):
        return redirect("home")
    else:
        model.completed = True
        model.save()
        return redirect("todo_list")


def todo_reactivate(request, pk):
    if "_auth_user_id" not in request.session:
        return redirect("/")
    model = ToDo.objects.get(pk=pk)
    if request.session["_auth_user_id"] != str(model.creator.pk):
        return redirect("home")
    else:
        model.completed = False
        model.save()
        return redirect("todo_list")


class ToDoListDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ToDoList
    template_name = "todo_list_detail.html"
    context_object_name = "todo_list"
    pk_url_kwarg = "pk"

    def test_func(self):
        todo_list = self.get_object()
        return todo_list.creator == self.request.user

    def get_queryset(self):
        return ToDoList.objects.filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todo_list = self.get_object()
        context["todo_list"] = ToDo.objects.filter(todo_list=todo_list)
        context["list_name"] = todo_list.title
        context["list_pk"] = todo_list.pk
        return context


class ToDoListCreateView(LoginRequiredMixin, CreateView):
    model = ToDoList
    form_class = ToDoListCreateForm
    template_name = "todo_list_new.html"
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ToDoListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDoList
    form_class = ToDoListUpdateForm
    template_name = "todo_list_edit.html"
    success_url = reverse_lazy("todo_list")

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class TodoListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDoList
    template_name = "todo_list_delete.html"
    success_url = reverse_lazy("todo_list")

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


def export_data(request):
    query_set = ToDo.objects.filter(creator=request.user.pk).order_by(
        "todo_list__title"
    )
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="exported_data.csv"'},
    )
    writer = csv.writer(response)

    writer.writerow(
        [
            "Title",
            "Details",
            "Important",
            "Urgent",
            "Due Date",
            "Completed",
            "ToDo List",
        ]
    )
    for item in query_set:
        writer.writerow(
            [
                item.title,
                item.details,
                item.important,
                item.urgent,
                item.due_date,
                item.completed,
                item.todo_list,
            ]
        )

    return response


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"
