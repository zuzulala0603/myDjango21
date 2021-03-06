# Generated by Django 3.1.2 on 2020-11-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='이메일'),
        ),
    ]
