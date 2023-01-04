from django.contrib import admin
from table.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "company_name",
        "qty",
        "file_name",
        "plate_size",
        "equipment",
        "add_data",
        "add_time",
        "punch",
        "stage",
        "operator",
        "ready_datatime",
    ]

    search_fields = [
        "company_name",
        "file_name",
        "equipment",
        "add_data"
    ]

    list_filter = [
        "equipment",
        "punch",
        "stage",
        "operator",
    ]

    list_per_page = 20


admin.site.register(Tasks, TasksAdmin)
