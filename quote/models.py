from django.db import models

# Create your models here.
class Quote(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),

    )
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=20)
    message=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100, choices=STATUS, default='New')

    def __str__(self):
        return self.first_name