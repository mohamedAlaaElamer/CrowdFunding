from django.db import models
from myuser.models import *
from project.models import *
# Create your models here.

class reportproject(models.Model):
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE)
    report_message = models.TextField()