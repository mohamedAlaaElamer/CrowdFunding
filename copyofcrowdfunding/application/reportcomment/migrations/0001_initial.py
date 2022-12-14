# Generated by Django 4.0.5 on 2022-07-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportcomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_message', models.TextField()),
                ('comment_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.comment')),
                ('myuser_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.myuser')),
            ],
        ),
    ]
