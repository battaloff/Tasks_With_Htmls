"""politext_tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from table import views

urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),
    # Home page
    path('', views.home, name='home'),



    # ADD Task
    path('add_task', views.add_task, name='add_task'),

    # View Task
    path('task_view/<str:task_id>', views.task_view, name='task_view'),

    # Edit Task
    path('edit_task', views.edit_task, name='edit_task'),

    # Delete Task
    path('delete_task/<str:task_id>', views.delete_task, name='delete_task'),

]
