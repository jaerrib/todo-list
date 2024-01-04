from django.urls import path

from .views import SignUpView, LogOutRenderView

urlpatterns = [
    path("logout/", LogOutRenderView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
