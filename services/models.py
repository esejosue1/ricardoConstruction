from django.db import models

# Create your models here.
class Services(models.Model):
    type_of_service=models.CharField(max_length=30)
    introduction=models.TextField(max_length=500)
    image=models.ImageField(upload_to='img/services')
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

    def __str__(self):
        return self.type_of_service