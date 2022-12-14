# Generated by Django 4.0.5 on 2022-07-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_message', models.TextField()),
                ('myuser_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.users')),
                ('on_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.comment')),
                ('project_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
