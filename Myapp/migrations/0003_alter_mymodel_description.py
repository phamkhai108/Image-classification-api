# Generated by Django 5.0.1 on 2024-02-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_mymodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
