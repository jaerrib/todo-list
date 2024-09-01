from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ToDoList, ToDo


class ToDotests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        cls.todo_list = ToDoList.objects.create(
            title="testlist",
            creator=cls.user,
        )

        cls.todo = ToDo.objects.create(
            title="testitem",
            details="some details here",
            important=True,
            urgent=False,
            due_date=None,
            completed=False,
            creator=cls.user,
            todo_list=cls.todo_list,
        )

    def test_todo_list(self):
        self.assertEqual(f"{self.todo_list.title}", "testlist")
        self.assertEqual(f"{self.todo_list.creator.username}", "testuser")

    def test_todo_list_view_for_logged_in_user(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.todo_list.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testlist")
        self.assertTemplateUsed(response, "todo_list_detail.html")

    def test_todo_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.todo_list.get_absolute_url())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/todos/lists/1/" % (reverse("login")))
        response = self.client.get("%s?next=/todos/lists/1/" % (reverse("login")))
        self.assertContains(response, "Log In")

    def test_todo(self):
        self.assertEqual(f"{self.todo.title}", "testitem")
        self.assertEqual(f"{self.todo.details}", "some details here")
        self.assertEqual(self.todo.important, True)
        self.assertEqual(self.todo.urgent, False)
        self.assertEqual(self.todo.due_date, None)
        self.assertEqual(self.todo.completed, False)
        self.assertEqual(f"{self.todo.creator.username}", "testuser")
        self.assertEqual(f"{self.todo_list.title}", "testlist")
