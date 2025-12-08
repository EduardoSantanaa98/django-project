from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    word_count = models.IntegerField(default=0)
  
   #Create your models here.
