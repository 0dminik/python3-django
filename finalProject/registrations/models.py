# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your models here.
class Registration(models.Model):
    class Meta:
        db_table = 'registration'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return '{}   {} {} {}'.format(self.id, self.first_name, self.last_name, self.email)


class Loging(models.Model):
    class Meta:
        db_table = 'loging'
    user_password = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50)

