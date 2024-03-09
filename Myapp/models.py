from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
