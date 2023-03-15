from django.shortcuts import render
from .models import Task

def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': task})

