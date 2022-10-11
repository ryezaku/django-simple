from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Score


class AdminAccount(UserAdmin):
    ordering = ('name',)
    list_display = ('name', 'score', 'result')
    search_fields = ('name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Score, AdminAccount)


