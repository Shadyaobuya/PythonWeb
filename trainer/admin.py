from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.Trainer)


@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "gender"]
    search_fields = ["full_name"]
