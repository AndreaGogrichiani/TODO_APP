from django.shortcuts import render

from .models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/home.html', {'todos': todos})
