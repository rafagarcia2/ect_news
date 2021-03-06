# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    # author = models.ForeignKey('auth.User', blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(
        upload_to='blog/images', verbose_name='Imagem',
        null=True, blank=True
    )
    # content = RichTextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
