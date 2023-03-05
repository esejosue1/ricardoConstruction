from django.db import models
from django.urls import reverse

# Create your models here.
class Services(models.Model):
    type_of_service=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30, unique=True, null=True)
    introduction=models.TextField(max_length=500)
    image=models.ImageField(upload_to='img/services')
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=500)

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

    def get_url(self):
        return reverse('serviceDetail', args=[self.slug])
    
    def __str__(self):
        return self.type_of_service