from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User as AdminUsers

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "username",
    ]


admin.site.unregister(Group)
admin.site.unregister(AdminUsers)
