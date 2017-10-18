from __future__ import unicode_literals
from datetime import date

from django.db import models

# Create your models here.
class News(models.Model):
    class Meta:
        db_table = 'news'

    image = models.ImageField(upload_to='news')
    title = models.CharField(max_length=104)
    sub_title = models.CharField(max_length=100)
    description = models.TextField(max_length=800)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.title, self.sub_title)

