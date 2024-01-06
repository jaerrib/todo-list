from django.urls import path

from .views import (
    HomePageView,
    ToDoListView,
    ToDoDetailView,
    ToDoCreateView,
    ToDoUpdateView,
    TodoDeleteView,
    todo_complete,
    todo_reactivate,
)

urlpatterns = [
    path("todos/", ToDoListView.as_view(), name="todo_list"),
    path("todos/new/", ToDoCreateView.as_view(), name="todo_new"),
    path("todos/<int:pk>/", ToDoDetailView.as_view(), name="todo_detail"),
    path("todos/<int:pk>/edit/", ToDoUpdateView.as_view(), name="todo_edit"),
    path("todos/<int:pk>/delete/", TodoDeleteView.as_view(),
         name="todo_delete"),
    path("todos/<int:pk>/complete/", todo_complete, name="todo_complete"),
    path("todos/<int:pk>/reactivate/", todo_reactivate, name="todo_reactivate"),
    path("", HomePageView.as_view(), name="home"),
]
