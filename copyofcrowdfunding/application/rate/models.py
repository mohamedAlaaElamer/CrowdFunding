from django.db import models

from myuser.models import *
from project.models import *
# Create your models here.

class rate(models.Model):
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE)
    rate_value = models.IntegerField()