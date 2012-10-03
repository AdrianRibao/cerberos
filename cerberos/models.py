# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.db import models
#from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _ 
#from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

class FailedAccessAttempt(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, verbose_name=_(u'Site'))
    ip_address = models.IPAddressField(verbose_name=_(u'IP Address'), null=True)
    user_agent = models.CharField(max_length=255, verbose_name=_(u'User Agent'), blank=False,
            help_text=_(u'User agent used in the login attempt'))
    username = models.CharField(max_length=255, verbose_name=_(u'Username'), blank=False,
            help_text=_(u'Username used to login'))
    failed_logins = models.PositiveIntegerField(verbose_name=_(u'Failed logins'),
            help_text=_(u'Failed logins for this IP'))

    get_data = models.TextField('GET Data')
    post_data = models.TextField('POST Data')
    http_accept = models.CharField('HTTP Accept', max_length=255)
    path_info = models.CharField('Path', max_length=255)

    class Meta:
        verbose_name = _(u'Failed access attempt')
        verbose_name_plural = _(u'Failed access attempts')
        
    def __unicode__(self):
        return u'%s: %s' % (self.username, self.ip_address )
