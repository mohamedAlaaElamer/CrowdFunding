from django.db import models
from myuser.models import *
from comment.models import *
# Create your models here.

class reply(models.Model):
    comment_obj = models.ForeignKey(comment,on_delete=models.CASCADE)
    myuser_obj = models.ForeignKey(Users,on_delete=models.CASCADE)
    reply_message = models.TextField()