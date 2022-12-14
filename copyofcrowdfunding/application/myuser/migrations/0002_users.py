# Generated by Django 3.2.14 on 2022-07-18 15:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('Confirm_Password', models.CharField(max_length=50)),
                ('Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('Profile_Picture', models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d')),
            ],
        ),
    ]
