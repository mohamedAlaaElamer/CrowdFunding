# Generated by Django 4.0.5 on 2022-07-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('iscofirm', models.BooleanField(default=True)),
                ('phonenumber', models.CharField(max_length=11)),
                ('profilepic', models.ImageField(upload_to='')),
            ],
        ),
    ]
