from django.shortcuts import render

from core_todo.models import Task, Tag


def index(request):
    """View function for the home page of the site."""

    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }

    return render(request, "core_todo/index.html", context=context)
