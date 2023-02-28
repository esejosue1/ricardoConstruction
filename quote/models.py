from django.db import models

# Create your models here.
class Quote(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    message=models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name