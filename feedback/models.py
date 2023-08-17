from django.db import models

# Create your models here.
class feedbackmodel(models.Model):
    Name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    Email=models.EmailField()
    mobile=models.PositiveBigIntegerField()
    desc=models.TextField(max_length=500)

