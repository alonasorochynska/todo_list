from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from core_todo.models import Tag, Task

User = get_user_model()


class TagModelTest(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Urgent")
        self.assertEqual(tag.name, "Urgent")
        self.assertEqual(str(tag), "Urgent")


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")
        self.task = Task.objects.create(
            title="Complete project",
            content="Finish the Django project by the end of the week",
            deadline=timezone.now() + timezone.timedelta(days=7),
            owner=self.user,
            priority="high"
        )
        self.task.tags.add(self.tag1, self.tag2)

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Complete project")
        self.assertEqual(self.task.content, "Finish the Django project by the end of the week")
        self.assertEqual(self.task.owner.username, "testuser")
        self.assertEqual(self.task.priority, "high")
        self.assertEqual(self.task.status, False)

    def test_task_absolute_url(self):
        self.assertEqual(self.task.get_absolute_url(), f"/tasks/{self.task.pk}/")

    def test_task_tags(self):
        self.assertIn(self.tag1, self.task.tags.all())
        self.assertIn(self.tag2, self.task.tags.all())

    def test_get_tags_names(self):
        self.assertEqual(self.task.get_tags_names(), "Work, Personal")
