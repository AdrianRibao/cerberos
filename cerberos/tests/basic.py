# -*- coding: utf-8 -*-
from django.test import TestCase
from django.test.client import Client
from cerberos.models import FailedAccessAttempt
from django.contrib.auth.models import User
import time

class RegisterAttemptsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = '/accounts/login/'

    def _perform_failed_login(self):
        response = self.client.post(self.login_url, {
            'username': 'demo',
            'password': 'demo',
            })
        return response

    def _generate_n_failed_logins(self, n):
        """
        Generate n failed_logins
        """
        for i in range(1, n+1):
            self._perform_failed_login()

    def test_record_failed_login(self):
        response = self._perform_failed_login()
        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)

        faa = qs[0]
        self.assertEqual(faa.ip_address, '127.0.0.1')
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 1)
        self.assertFalse(faa.locked)
        self.assertFalse(faa.expired)

    def test_two_failed_logins(self):
        self._generate_n_failed_logins(2)

        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)
        faa = qs[0]
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 2)
        self.assertFalse(faa.locked)
        self.assertFalse(faa.expired)

    def test_three_failed_logins(self):
        self._generate_n_failed_logins(3)

        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)
        faa = qs[0]
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 3)
        self.assertTrue(faa.locked)
        self.assertFalse(faa.expired)

    def test_four_failed_logins(self):
        self._generate_n_failed_logins(4)

        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)
        faa = qs[0]
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 4)
        self.assertTrue(faa.locked)
        self.assertFalse(faa.expired)

    def test_access_login_url_after_being_locked(self):
        self._generate_n_failed_logins(4)
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('user-locked.html')
        self.assertContains(response, '<h2>Access locked</h2>')

    def test_access_login_url_via_post_after_being_locked(self):
        self._generate_n_failed_logins(4)
        response = self.client.post(self.login_url, {
            'username': 'demo',
            'password': 'demo',
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('user-locked.html')
        self.assertContains(response, '<h2>Access locked</h2>')

    def test_access_login_url_via_post_after_being_locked_with_valid_user(self):
        user = User.objects.create_user('valid_user', 'valid_user@example.com', 'valid_password')
        self._generate_n_failed_logins(4)
        response = self.client.post(self.login_url, {
            'username': 'valid_user',
            'password': 'valid_password',
            })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('user-locked.html')
        self.assertContains(response, '<h2>Access locked</h2>')

    def test_valid_login_after_one_failed_attempt(self):
        user = User.objects.create_user('demo', 'demo@example.com', 'valid_password')
        self._generate_n_failed_logins(1)
        response = self.client.post(self.login_url, {
            'username': 'demo',
            'password': 'valid_password',
            })
        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)
        faa = qs[0]
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 1)
        self.assertFalse(faa.locked)
        self.assertTrue(faa.expired)

    def test_expire_attempt_after_timeout(self):
        from cerberos import models
        models.MEMORY_FOR_FAILED_LOGINS = 1

        self._generate_n_failed_logins(4)
        qs = FailedAccessAttempt.objects.all()
        self.assertEqual(qs.count(), 1)
        faa = qs[0]
        
        # Wait for the attempt to expire
        time.sleep(2)

        # Create a valid login
        user = User.objects.create_user('demo', 'demo@example.com', 'valid_password')
        response = self.client.post(self.login_url, {
            'username': 'demo',
            'password': 'valid_password',
            })
        qs = FailedAccessAttempt.objects.all()
        faa = qs[0]
        self.assertEqual(faa.username, 'demo')
        self.assertEqual(faa.failed_logins, 4)
        self.assertTrue(faa.locked)
        self.assertTrue(faa.expired)

