from django.db import models
from django.contrib.auth.models import User


class Communities(models.Model):
    name = models.CharField('Название', max_length=75)
    description = models.TextField('Описание', max_length=150)
    slug = models.SlugField('Служебный код')
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField('Свободный вход')
    avatar = models.ImageField('Аватар', default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name
# Create your models here.
