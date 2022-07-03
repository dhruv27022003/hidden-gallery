from datetime import datetime
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField



class file_upload(models.Model):
    ids=  models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=200)
    my_file= models.FileField(upload_to='')
    
  
def __str__(self):
        return self.file_name
