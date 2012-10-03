# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from cerberos.models import FailedAccessAttempt
from cerberos.settings import MAX_FAILED_LOGINS

def watch_logins(func):

    def new_func(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if request.method == 'POST' and response.status_code != 302:
            process_failed_login(request)
        return response
    return new_func

def process_failed_login(request):
    site = Site.objects.get_current()
    ip = request.META.get('REMOTE_ADDR', '')
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    username = request.POST.get('username')
    http_accept = request.META.get('HTTP_ACCEPT', 'unknown'),
    path_info = request.META.get('PATH_INFO', 'unknown')
    
    try:
        fa = FailedAccessAttempt.objects.get(ip_address=ip)
    except:
        fa = FailedAccessAttempt(ip_address=ip)
    fa.site = site
    fa.user_agent = user_agent
    fa.username = username
    fa.failed_logins += 1
    fa.get_data = request.GET
    fa.post_data = request.POST
    fa.http_accept = http_accept
    fa.path_info = path_info
    fa.save()

    if fa.failed_logins >= MAX_FAILED_LOGINS:
        print "BLOQUEAR!!!"
