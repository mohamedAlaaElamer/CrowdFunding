from django.db import models
from myuser.models import *
from comment.models import *
# Create your models here.

class reportcomment(models.Model):
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    comment_obj = models.ForeignKey(comment,on_delete=models.CASCADE)
    report_message = models.TextField()