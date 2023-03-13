from django.db import models
# from django.contrib.auth.models import User


# Create your models here.
class movies(models.Model):
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media')
    duration=models.DurationField()
    
    def __str__(self):
        return self.Name
