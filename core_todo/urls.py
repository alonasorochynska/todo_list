from django.urls import path

from core_todo.views import index, TaskListView, TagListView, TaskDetailView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    ]

app_name = "core_todo"
