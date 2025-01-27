from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import ToDoItems


# from models import ToDoItems


# Create your views here.
def home(request):
    # return HttpResponse('Hello, world!')
    return render(request, 'home.html')


def handle_params(request, param1):
    return HttpResponse(f'param1 is {param1}')


def todos(request):
    items = ToDoItems.objects.all()
    return render(request, 'todos.html', {"todos": items})
