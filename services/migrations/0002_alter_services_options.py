# Generated by Django 4.1.7 on 2023-03-03 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
