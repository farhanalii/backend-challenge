from django.test import TestCase, Client
from django.contrib.auth.models import User
from tasks.models import Task, Label

class TaskPermissionsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username='testuser1', password='12345')
        self.user2 = User.objects.create_user(username='testuser2', password='12345')
        self.client.login(username='testuser1', password='12345')
        self.label = Label.objects.create(name='Test Label', owner=self.user1)
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user1)
        self.task.labels.add(self.label)

    def test_task_permissions(self):
        # User 1 should have access to their task
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)

        # User 2 should not have access to User 1's task
        self.client.login(username='testuser2', password='12345')
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 403)
