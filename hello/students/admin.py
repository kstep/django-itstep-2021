from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    pass
