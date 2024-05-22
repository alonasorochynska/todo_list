from django.urls import path

from core_todo.views import index


urlpatterns = [
    path("", index, name="index"),
    ]

app_name = "core_todo"
