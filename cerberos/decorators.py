# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from cerberos.models import FailedAccessAttempt
from cerberos.settings import MAX_FAILED_LOGINS, MEMORY_FOR_FAILED_LOGINS
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

def watch_logins(func):

    def new_func(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        ip = request.META.get('REMOTE_ADDR', '')

        failed_access = get_failed_access(ip)

        failed_access = check_failed_login(request, response, failed_access)

        if failed_access.locked:
            response = get_locked_response(request, ip, failed_access)

        return response
    return new_func

def get_failed_access(ip):
    """
    Returns the FailedAccessAttempt object for a given IP.
    """
    try:
        failed_access = FailedAccessAttempt.objects.get(ip_address=ip)
    except FailedAccessAttempt.DoesNotExist:
        failed_access = None

    if failed_access:
        time_remaining = failed_access.get_time_to_forget()
        if time_remaining != None and time_remaining <= 0:
            failed_access.delete()
            failed_access = None

    return failed_access


def check_failed_login(request, response, failed_access):
    """
    If is a failed login, save the data in the database.

    It returns the FailedAccessAttempt instance.
    """
    site = Site.objects.get_current()
    ip = request.META.get('REMOTE_ADDR', '')
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    username = request.POST.get('username')
    http_accept = request.META.get('HTTP_ACCEPT', 'unknown'),
    path_info = request.META.get('PATH_INFO', 'unknown')

    
    if not failed_access:
        failed_access = FailedAccessAttempt(ip_address=ip)

    if request.method == 'POST' and response.status_code != 302:
        # Failed login
        failed_access.site = site
        failed_access.user_agent = user_agent
        failed_access.username = username
        failed_access.failed_logins += 1
        failed_access.get_data = request.GET
        failed_access.post_data = request.POST
        failed_access.http_accept = http_accept
        failed_access.path_info = path_info

        if failed_access.failed_logins >= MAX_FAILED_LOGINS:
            # Lock the user
            failed_access.locked = True
        failed_access.save()
    elif request.method == 'POST' and response.status_code == 302 and failed_access.id:
        # The user logged in successfully. Forgets about the access attempts
        failed_access.delete()

    return failed_access

def get_locked_response(request, ip, failed_access):
    return render_to_response('cerberos/user-locked.html',
                              {
                                  'ip':ip,
                                  'failed_access': failed_access,
                                  },
                              context_instance=RequestContext(request))
