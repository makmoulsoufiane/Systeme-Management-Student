# Group/admin.py
from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'year_of_creation')
