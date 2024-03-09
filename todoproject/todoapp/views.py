from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/home.html', {'todos': todos})

def add_todo(request):
    return HttpResponse("HI")