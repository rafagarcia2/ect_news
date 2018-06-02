from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User', blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField('Atalho')
    # text = models.TextField()
    # image = models.ImageField(
    #     upload_to='blog/images', verbose_name='Imagem',
    #     null=True, blank=True
    # )
    content = RichTextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        return ('post:post_detail', (), {'slug': self.slug})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class AbaPrincipal(models.Model):

    name = models.CharField('Nome', max_length=20)
    link = models.CharField('link', max_length=50)
    is_active = models.BooleanField('Está ativo?')
    compost = models.BooleanField('É composto?')

    def __str__(self):
        return self.name
