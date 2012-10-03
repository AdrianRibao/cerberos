# -*- coding: utf-8 -*-
from django.contrib import admin
from cerberos.models import FailedAccessAttempt

class FailedAccessAttemptAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = [
            'ip_address',
            'username',
            'user_agent',
            'failed_logins',
            'site',
            ]
    list_filter = [
            'site',
            ]
    search_fields = [
            'ip_address',
            'username',
            'user_agent',
            ]
    fieldsets = (
        ('Main data', {
            'fields': ('site', 'ip_address', 'username', 'failed_logins', )
        }),
        ('Data recollected', {
            #'classes': ('collapse',),
            'fields': ('user_agent', 'get_data', 'post_data', 'http_accept', 'path_info',)
        }),
    )
admin.site.register(FailedAccessAttempt, FailedAccessAttemptAdmin)
