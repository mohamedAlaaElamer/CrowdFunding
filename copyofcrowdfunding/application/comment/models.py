from django.db import models
from myuser.models import *
from project.models import *
# Create your models here.

class comment(models.Model):
    id = models.AutoField(primary_key=True)
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE)
    comment_message = models.TextField()
    on_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True ,blank=True)