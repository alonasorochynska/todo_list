from django.urls import path

from core_todo.views import index, TaskListView, TagListView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    ]

app_name = "core_todo"
