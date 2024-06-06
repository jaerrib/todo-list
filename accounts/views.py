from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogOutRenderView(TemplateView):
    template_name = "home.html"


class AccountDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "registration/account_delete.html"
    success_url = reverse_lazy("home")

    def get_queryset(self):
        query_set = User.objects.filter(pk=self.request.user.pk)
        return query_set

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
