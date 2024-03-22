from django.db import models
from django.urls import reverse


class ToDoList(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_list_detail", kwargs={"pk": self.pk})


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True, null=True)
    important = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    creator = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    todo_list = models.ForeignKey(
        "ToDoList",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
