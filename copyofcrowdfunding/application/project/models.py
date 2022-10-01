from django.db import models
from myuser.models import *
from category.models import *
# Create your models here.

def change_path(instance , filename):
    return "project"+str(instance.project_obj.id)+ "/"+filename

def change_path_proj(instance , filename):
    return "projectposters"+"/"+filename

class project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    details = models.CharField(max_length=100)
    target = models.FloatField()
    startdate = models.DateField()
    enddate = 	models.DateField()
    poster = models.ImageField()
    cat = models.ForeignKey(category,on_delete=models.CASCADE)
    createdby= models.ForeignKey(Users,on_delete=models.CASCADE)


class project_tags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE)
    tag = models.CharField(max_length=25)



class project_pic(models.Model):
    pic_id = models.AutoField(primary_key=True)
    project_obj = models.ForeignKey(project,on_delete=models.CASCADE,null=False)
    picture = models.ImageField()