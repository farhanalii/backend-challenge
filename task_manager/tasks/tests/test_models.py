from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task, Label

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.label = Label.objects.create(name='Test Label', owner=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user)
        self.task.labels.add(self.label)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.owner, self.user)
        self.assertTrue(self.task.labels.exists())

    def test_label_creation(self):
        self.assertEqual(self.label.name, 'Test Label')
        self.assertEqual(self.label.owner, self.user)