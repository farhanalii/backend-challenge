from django.test import TestCase, Client
from django.contrib.auth.models import User
from tasks.models import Task, Label

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.label = Label.objects.create(name='Test Label', owner=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user)
        self.task.labels.add(self.label)

    def test_task_list_create_view(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_retrieve_update_destroy_view(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Task')
