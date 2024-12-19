from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField('Заголовок', max_length=75)
    body = models.TextField('Пост')
    slug = models.SlugField('Служебный код')
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField('Картинка', default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.title
# Create your models here.
