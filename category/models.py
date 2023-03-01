from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    job_category=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    job_descrition=models.TextField(max_length=200)

    class Meta:
        verbose_name='job_category'
        verbose_name_plural='job_categories'
    def get_url(self):
        return reverse('job_by_category', args=[self.slug])
    def __str__(self):
        return self.job_category