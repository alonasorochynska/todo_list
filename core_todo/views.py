from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from core_todo.forms import TaskCreateForm, TagCreateForm, TaskSearchForm, TaskUpdateForm
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
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.request.GET.get("tag", "")
        context["search_form"] = TaskSearchForm(initial={"tag": tag})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            tag_name = form.cleaned_data["tag"]
            if tag_name:
                queryset = queryset.filter(tags__name__icontains=tag_name)
        return queryset


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


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("core_todo:task-list")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "core_todo/tag_form.html"
    success_url = reverse_lazy("core_todo:tag-list")
