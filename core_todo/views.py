from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from core_todo.forms import TaskCreateForm
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


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")
    # paginate_by = 5


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "core_todo/task_form.html"
    success_url = reverse_lazy("core_todo:task-list")


class CompleteTaskView(LoginRequiredMixin, generic.TemplateView):
    @staticmethod
    def post(request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.status = True
        task.save()
        return redirect(reverse("core_todo:task-list"))


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
