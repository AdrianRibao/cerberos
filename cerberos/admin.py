# -*- coding: utf-8 -*-
from django.contrib import admin
from cerberos.models import FailedAccessAttempt
from django.utils.translation import ugettext as _ 

class FailedAccessAttemptAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = [
            'ip_address',
            'username',
            'locked',
            'user_agent',
            'failed_logins',
            'get_time_to_forget_text',
            'site',
            ]
    list_filter = [
            'locked',
            'site',
            ]
    search_fields = [
            'ip_address',
            'username',
            'user_agent',
            ]
    fieldsets = (
        ('Main data', {
            'fields': ('site', 'ip_address', 'username', 'locked', 'failed_logins', )
        }),
        ('Data recollected', {
            #'classes': ('collapse',),
            'fields': ('user_agent', 'get_data', 'post_data', 'http_accept', 'path_info',)
        }),
    )
    actions = ['lock', 'unlock']

    def lock(self, request, queryset):
        queryset.update(locked=True)
    lock.short_description = _(u'Lock the users')

    def unlock(self, request, queryset):
        queryset.update(locked=False)
    unlock.short_description = _(u'Unlock the users')

admin.site.register(FailedAccessAttempt, FailedAccessAttemptAdmin)
