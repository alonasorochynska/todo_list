from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    done_time = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default="medium")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")

    def __str__(self):
        return (f"Task: {self.content[:20]}... |"
                f" Created at: {self.created_time} |"
                f" Deadline: {self.deadline}"
                f" Completed: {self.done_time} |"
                f" Priority: {self.priority}")

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["done_time", "-created_time"]

    def get_absolute_url(self):
        return reverse("core_todo:task-detail", kwargs={"pk": self.pk})

    def get_tags_names(self):
        return ", ".join(tag.name for tag in self.tags.all())
