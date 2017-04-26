# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170112_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'blog/images', null=True, verbose_name=b'Imagem', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
