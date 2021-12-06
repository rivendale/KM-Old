from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    memory = models.CharField(max_length=1500)
    category = models.CharField(max_length=15)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False) 

class Files(models.Model):
    file = models.FileField(upload_to='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
