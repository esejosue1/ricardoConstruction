from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from ricardoConstruction.utils import unique_slug_genereator


# Create your models here.
class Services(models.Model):
    title=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30, unique=True, null=True, blank=True)
    introduction=models.TextField(max_length=500)
    image=models.ImageField(upload_to='img/services')
    
    description=models.TextField(max_length=500)

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

    def get_url(self):
        return reverse('serviceDetail', args=[self.slug])
    
    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_genereator(instance)

pre_save.connect(slug_generator, sender=Services)

