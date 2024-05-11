from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('labels/', views.LabelList.as_view(), name='label-list'),
    path('labels/<int:pk>/', views.LabelDetail.as_view(), name='label-detail'),
]