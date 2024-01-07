from django import forms
from django.forms import ModelForm

from .models import ToDo


class DateInput(forms.DateInput):
    input_type = "date"


class ToDoCreateForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ["title", "details", "important", "urgent", "due_date"]
        widgets = {
            "due_date": DateInput(),
        }


class ToDoUpdateForm(ModelForm):
    class Meta:
        model = ToDo
        fields = [
            "title",
            "details",
            "important",
            "urgent",
            "completed",
            "due_date",
        ]
        widgets = {
            "due_date": DateInput(),
        }
