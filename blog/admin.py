from django.contrib import admin
from .models import Post, AbaPrincipal


class PostAdmin(admin.ModelAdmin):

    list_display = ['author', 'title', 'slug', 'content', 'created_date', 'published_date']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(AbaPrincipal)
