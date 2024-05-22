from django.test import TestCase
from django.contrib.auth import get_user_model
from core_todo.models import Task, Tag
from core_todo.forms import TaskCreateForm, TaskUpdateForm, TaskSearchForm, TagCreateForm

User = get_user_model()


class TaskCreateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.tag1 = Tag.objects.create(name="Urgent")
        self.tag2 = Tag.objects.create(name="Work")

    def test_task_create_form_valid_data(self):
        form = TaskCreateForm(data={
            "title": "Test Task",
            "content": "This is a test task.",
            "deadline": "2024-05-22",
            "owner": self.user.id,
            "priority": "medium",
            "tags": [self.tag1.id, self.tag2.id]
        })
        self.assertTrue(form.is_valid())


class TaskUpdateFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.task = Task.objects.create(
            title="Test Task",
            content="This is a test task.",
            owner=self.user,
            priority="medium"
        )

    def test_task_update_form_valid_data(self):
        form = TaskUpdateForm(data={
            "owner": self.user.id,
            "deadline": "2024-05-22",
            "priority": "high",
            "content": "Updated content",
            "tags": []
        }, instance=self.task)
        self.assertTrue(form.is_valid())


class TaskSearchFormTest(TestCase):
    def test_task_search_form_valid_data(self):
        form = TaskSearchForm(data={"tag": "Urgent"})
        self.assertTrue(form.is_valid())


class TagCreateFormTest(TestCase):
    def test_tag_create_form_valid_data(self):
        form = TagCreateForm(data={"name": "Urgent"})
        self.assertTrue(form.is_valid())
