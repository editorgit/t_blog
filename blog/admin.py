from django.contrib import admin

from blog.models import Article, Writer


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_editor', 'user')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
