from django.test import TestCase
from django.contrib.auth.models import User
from tasks.models import Task, Label
from tasks.serializers import TaskSerializer, LabelSerializer

class SerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.label = Label.objects.create(name='Test Label', owner=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', owner=self.user)
        self.task.labels.add(self.label)

    def test_task_serializer(self):
        serializer = TaskSerializer(instance=self.task)
        self.assertEqual(serializer.data['title'], 'Test Task')
        self.assertEqual(serializer.data['description'], 'Test Description')
        self.assertEqual(serializer.data['owner'], self.user.id)
        label_name = Label.objects.get(id=serializer.data['labels'][0])
        self.assertTrue(label_name, 'Test Label')


    def test_label_serializer(self):
        serializer = LabelSerializer(instance=self.label)
        self.assertEqual(serializer.data['name'], 'Test Label')
        self.assertEqual(serializer.data['owner'], self.user.id)
