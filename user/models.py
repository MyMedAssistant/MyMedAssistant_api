from django.db import models

# Create your models here.

class User(models.Model):
  user_name = models.CharField(max_length=64)
  user_email = models.CharField(max_length=64)
  oauth_token = models.CharField(max_length=64)
  phone = models.IntegerField()
  doc_name = models.CharField(max_length=64)
  doc_phone = models.IntegerField()
  doc_clinic = models.CharField(max_length=64)


  def __str__(self):
    return self.user_name
