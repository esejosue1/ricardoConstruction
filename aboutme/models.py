from django.db import models


class CompanyInfo(models.Model):
    company_name=models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    unit = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    watsapp = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name='Company Info'

    def __str__(self):
        return self.company_name
    

# Create your models here.
class Employees(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    chief=models.BooleanField(default=False)
    manager=models.BooleanField(default=False)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/team')
    description=models.CharField(max_length= 250)

    class Meta:
        verbose_name='Employee'
        verbose_name_plural='Employees'

    def __str__(self):
        return self.last_name


