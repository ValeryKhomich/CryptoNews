from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)  # Заголовок
    description = models.TextField(blank=True, null=True)  # Краткое описание
    content = models.TextField()  # Полный текст статьи
    image_url = models.URLField(max_length=500, blank=True, null=True)  # Ссылка на изображение
    source = models.CharField(max_length=255, blank=True, null=True)  # Источник
    published_at = models.DateTimeField(default=timezone.now)  # Дата публикации

    def __str__(self):
        return self.title
