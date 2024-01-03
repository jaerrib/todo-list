from django.db import models
from django.urls import reverse


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    important = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    due_date = models.DateField()
    creator = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
