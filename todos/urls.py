from django.urls import path

from .views import (
    HomePageView,
    ToDoListView,
    ToDoDetailView,
    ToDoCreateView,
    ToDoUpdateView,
    TodoDeleteView,
    ToDoCompleteView,
)

urlpatterns = [
    path("todos/", ToDoListView.as_view(), name="todo_list"),
    path("todos/new/", ToDoCreateView.as_view(), name="todo_new"),
    path("todos/<int:pk>/", ToDoDetailView.as_view(), name="todo_detail"),
    path("todos/<int:pk>/edit/", ToDoUpdateView.as_view(), name="todo_edit"),
    path("todos/<int:pk>/delete/", TodoDeleteView.as_view(),
         name="todo_delete"),
    path("todos/<int:pk>/complete/", ToDoCompleteView.as_view(),
         name="todo_complete"),
    path("", HomePageView.as_view(), name="home"),
]
