from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User, Tag, Task


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name",)


admin.site.register(Tag)
admin.site.register(Task)
admin.site.unregister(Group)
