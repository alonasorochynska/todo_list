from django.urls import path

from core_todo.views import index, TaskListView, TagListView, TaskDetailView, CompleteTaskView, TaskCreateView, \
    TagCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/complete/", CompleteTaskView.as_view(), name="task-complete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    ]

app_name = "core_todo"
