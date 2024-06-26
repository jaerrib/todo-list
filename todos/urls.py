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
    ToDoListDetailView,
    ToDoListCreateView,
    ToDoListUpdateView,
    TodoListDeleteView,
    export_data,
    PrivacyPolicyView,
)

urlpatterns = [
    path("todos/", ToDoListView.as_view(), name="todo_list"),
    path("todos/export/", export_data, name="export_data"),
    path("todos/<int:pk>/", ToDoDetailView.as_view(), name="todo_detail"),
    path(
        "todos/new/<int:todo_list_pk>/",
        ToDoCreateView.as_view(),
        name="todo_new",
    ),
    path("todos/<int:pk>/edit/", ToDoUpdateView.as_view(), name="todo_edit"),
    path("todos/<int:pk>/delete/", TodoDeleteView.as_view(),
         name="todo_delete"),
    path("todos/<int:pk>/complete/", todo_complete, name="todo_complete"),
    path("todos/<int:pk>/reactivate/", todo_reactivate, name="todo_reactivate"),
    path("todos/lists/new/", ToDoListCreateView.as_view(),
         name="todo_list_new"),
    path(
        "todos/lists/<int:pk>/", ToDoListDetailView.as_view(),
        name="todo_list_detail"
    ),
    path(
        "todos/lists/<int:pk>/edit/",
        ToDoListUpdateView.as_view(),
        name="todo_list_edit",
    ),
    path(
        "todos/lists/<int:pk>/delete/",
        TodoListDeleteView.as_view(),
        name="todo_list_delete",
    ),
    path("legal/privacy-policy/", PrivacyPolicyView.as_view(),
         name="privacy-policy"),
    path("", HomePageView.as_view(), name="home"),
]
