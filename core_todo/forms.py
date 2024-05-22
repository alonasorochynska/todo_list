from django import forms
from django.forms import DateInput

from core_todo.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Task
        fields = ("title", "content", "deadline", "owner", "priority", "tags")

        widgets = {
            "deadline": DateInput(attrs={"type": "date"}),
        }


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
