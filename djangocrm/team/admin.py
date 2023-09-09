from django.contrib import admin
from team.models import UserModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
    fields = ('first_name', 'last_name', 'phone', 'email')

    