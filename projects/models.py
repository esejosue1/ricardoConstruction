from django.db import models
from category.models import Category

# Create your models here.
class Projects(models.Model):
    project_title=models.CharField(max_length=150)
    project_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    project_img=models.ImageField(upload_to='img/projects')
    project_descrption=models.TextField(max_length=1000)
    project_client=models.CharField(max_length=150)
    project_date=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.project_title