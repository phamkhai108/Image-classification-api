# Generated by Django 5.0.1 on 2024-03-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_remove_mymodel_description_remove_mymodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]