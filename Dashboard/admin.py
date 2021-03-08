from django.contrib import admin
from .models import tasks
# Register your models here.
@admin.register(tasks)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","user","date","RevisionDate","TotalRevision","marked")