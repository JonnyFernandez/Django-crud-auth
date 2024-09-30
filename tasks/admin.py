from django.contrib import admin
from .models import Task


# como created se crea automaticamente, no me aparece en el admin, de esta manera hacemos que aparezca
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)


# Register your models here.
admin.site.register(Task, TaskAdmin)
