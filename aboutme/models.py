from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/team')
    description=models.CharField(max_length= 250)

    class Meta:
        verbose_name='Employee'
        verbose_name_plural='Employees'

    def __str__(self):
        return self.last_name

