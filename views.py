from django.shortcuts import render
from .models import Task  # if you have a Task model

def home(request):
    tasks = Task.objects.all()  # remove this line if you don’t have a model
    return render(request, 'home.html', {'tasks': tasks})
