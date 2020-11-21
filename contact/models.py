import os
from django.conf import settings
from django.db import models

class Contact(models.Model):
    writer = models.CharField(max_length=128, verbose_name='제목')
    email = models.CharField(max_length=128, verbose_name='이메일')
    content = models.CharField(max_length=128, verbose_name='내용')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'contact_table'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'