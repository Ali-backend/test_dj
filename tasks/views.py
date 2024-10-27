from django.shortcuts import render
from django.contrib.auth.models import User
from tasks.forms import TaskForm


def register_task(request):
    if request.method == 'GET':
        return render(request, 'users/register.tasks.html', context={"form": TaskForm})


