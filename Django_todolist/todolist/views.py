from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Todo

# class Todo:
#
#     def __init__(self, descrition, isCompleted):
#         self.descrition = descrition
#         self.isCompleted = isCompleted


def todo_list(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == 'add':
            title = request.POST.get('title')
            Todo.objects.create(title=title)

    list = Todo.objects.all()
    return render(request, 'todolist.html', locals())


def complete(request, id):
    todo_item = get_object_or_404(Todo, id = id)
    todo_item.completed = True
    todo_item.save()
    return HttpResponseRedirect('/')


def delete(request, pk):
    todo_item = get_object_or_404(Todo, id = pk)
    todo_item.delete()
    return HttpResponseRedirect('/')