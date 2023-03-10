# Generated by Django 4.1.7 on 2023-03-03 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(max_length=30)),
                ('introduction', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='img/services')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
