from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Tasks


# rendering home page
def home(request):
    task_list = Tasks.objects.all()
    context = {"task_list": task_list}
    return render(request, 'home.html', context)


# add task func
def add_task(request):
    if request.method == 'POST':
        if request.POST.get('company_name') \
                and request.POST.get('qty') \
                and request.POST.get('file_name') \
                and request.POST.get('plate_size') \
                and request.POST.get('punch'):
            task = Tasks()
            task.company_name = request.POST.get('company_name')
            task.qty = request.POST.get('qty')
            task.file_name = request.POST.get('file_name')
            task.plate_size = request.POST.get('plate_size')
            task.punch = request.POST.get('punch')
            task.save()
            messages.success(request, 'Молодец, спасибо !')
            return HttpResponseRedirect('/')
    else:
        return render(request, 'add_task')


# View task func
def task_view(request, task_id):
    task = Tasks.object.get(id=Tasks.id)
    if task != None:
        return render(request, 'edit_task.html', {'task': task})


# Edit task func
def edit_task(request):
    if request.method == 'POST':
        task = Tasks.objects.get(id=request.POST.get('id'))
        if task != None:
            task.company_name = request.POST.get('company_name')
            task.qty = request.POST.get('qty')
            task.file_name = request.POST.get('file_name')
            task.plate_size = request.POST.get('plate_size')
            task.punch = request.POST.get('punch')
            task.save()
            messages.success(request, 'Обновлено !')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'add_task')


# Delete task func
def delete_task(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    messages.success(request, 'Задача удалена')
    return HttpResponseRedirect('/')

