from django.db import models
from django.contrib.auth.models import User


class Label(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'owner')

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True, null=True)

    # Below are the enhancements made in the task module.
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True)
    attachments = models.FileField(upload_to='task_attachments/', null=True, blank=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.title
