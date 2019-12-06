from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    todolist = Todo.objects.all()
    return render(request, 'main/index.html', {'todolist': todolist})


def add_todo(request):
    added_date = timezone.now()
    added_text = request.POST["text"]
    id = Todo.objects.create(text=added_text, added_date=added_date)
    return HttpResponseRedirect(reverse('todo_home'))
