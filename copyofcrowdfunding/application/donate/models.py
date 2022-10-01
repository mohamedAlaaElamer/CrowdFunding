from django.db import models
from myuser.models import *
from project.models import *
# Create your models here.

class donate(models.Model):
    id = models.AutoField(primary_key=True)
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE)
    amount = models.FloatField()