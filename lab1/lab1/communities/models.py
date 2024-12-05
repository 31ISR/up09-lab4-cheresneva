from django.db import models

class Communities(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField()

    def __str__(self):
        return self.name
# Create your models here.
