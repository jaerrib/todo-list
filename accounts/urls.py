from django.urls import path

from .views import SignUpView, LogOutRenderView, AccountDeleteView

urlpatterns = [
    path("logout/", LogOutRenderView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("delete/<int:pk>/", AccountDeleteView.as_view(), name="account_delete"),
]
