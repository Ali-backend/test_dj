"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import TasklistView, TaskDetailView, TaskCreateView

# urls.py


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),          # URL для списка задач
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),  # URL для деталей задачи
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),  # URL для создания новой задачи
]

