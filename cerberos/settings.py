from django.conf import settings

MAX_FAILED_LOGINS = getattr(settings, 'MAX_FAILED_LOGINS', 3)
