# Generated by Django 4.1.7 on 2023-03-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0003_alter_employees_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='chief',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employees',
            name='manager',
            field=models.BooleanField(default=False),
        ),
    ]
