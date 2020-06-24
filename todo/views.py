from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from . models import Todo
from .forms import TodoForm, NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=form.cleaned_data['text'])
        new_todo.save()
    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')



# Using Modelforms

def home(request):
    todo_list = Todo.objects.order_by('id')

    newTodoForm = NewTodoForm()

    context = {'todo_list': todo_list, 'form': NewTodoForm}
    return render(request, 'todo/home.html', context)

# @require_POST
# def addTodo(request):
#     form = TodoForm(request.POST)
#
#     if form.is_valid():
#         new_todo = Todo(text=request.POST['text'])
#         new_todo.save()
#
#     return redirect('index')

@require_POST
def addTodoNew(request):
    newtodoform = NewTodoForm(request.POST)

    if newtodoform.is_valid():

        new_todo = newtodoform.save()
    return redirect('new')


def completeTodoNew(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('new')


def deleteCompletedNew(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('new')


def deleteAllNew(request):
    Todo.objects.all().delete()
    return redirect('new')