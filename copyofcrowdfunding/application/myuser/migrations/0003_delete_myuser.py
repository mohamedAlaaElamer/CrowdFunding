# Generated by Django 3.2.14 on 2022-07-18 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_users'),
        ('project', '0002_alter_project_createdby'),
        ('rate', '0002_alter_rate_myuser_obj'),
        ('reportcomment', '0002_alter_reportcomment_myuser_obj'),
        ('reply', '0002_alter_reply_myuser_obj'),
        ('donate', '0002_alter_donate_myuser_obj'),
        ('reportproject', '0002_alter_reportproject_myuser_obj'),
        ('comment', '0002_alter_comment_myuser_obj'),
    ]

    operations = [
        migrations.DeleteModel(
            name='myuser',
        ),
    ]