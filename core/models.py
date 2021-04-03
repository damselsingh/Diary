from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    defineday = models.CharField(max_length=50, default='Great Day')
    date = models.DateField(auto_now_add=True)
    write = models.TextField()