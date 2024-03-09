from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm


def home(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/home.html', {'todos': todos})

def add_todo(request):
    submitted = False
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/submitpage/')
    else:
        form = TodoForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'todoapp/add_todo.html', {'form': form, 'submitted': submitted})


def submitpage(request):
    return render(request, 'todoapp/submitpage.html')
