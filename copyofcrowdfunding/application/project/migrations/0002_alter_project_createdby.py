# Generated by Django 3.2.14 on 2022-07-18 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_users'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='createdby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.users'),
        ),
    ]
