from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Score(models.Model):
    name = models.CharField('name',max_length = 200)
    score = models.IntegerField('score') 
    result = models.FloatField('result', default = 0)
   
