from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


from .models import Task
from .forms import TodoListForm

def todolist(request):
    todo_list = Task.objects.order_by('-submission_date')

    form = TodoListForm()


    context = {'todo_list': todo_list, 'form' : form}

    return render(request, 'todolist/todolist.html', context)

@require_POST
def addTask(request):
    form = TodoListForm(request.POST)

    print(request.POST['text'])

    if form.is_valid():
        new_task = Task(text=request.POST['text'])
        new_task.save()

    return redirect('todolist')


def completeTask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = True
    task.save()

    return redirect('todolist')

def deleteCompleted(request):
    Task.objects.filter(complete__exact=True).delete()
    return redirect('todolist')

def deleteAll(request):
    Task.objects.all().delete()
    return redirect('todolist')
