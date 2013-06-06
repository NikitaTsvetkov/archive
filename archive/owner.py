from django.db import models

class Owner(models.Model):
    username     = models.CharField(max_length=30)
    password_hsh = models.TextField()
    class Meta:
        abstract = true
    
class Ownable(models.Model):
    