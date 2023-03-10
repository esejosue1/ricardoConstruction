# Generated by Django 4.1.7 on 2023-03-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=150)),
                ('project_img', models.ImageField(upload_to='img/projects')),
                ('project_descrption', models.TextField(max_length=1000)),
                ('project_client', models.CharField(max_length=150)),
                ('project_date', models.DateTimeField(auto_now_add=True)),
                ('project_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
