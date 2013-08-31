from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status', 'created', 'modified')
    list_display_links = ('id', 'title', 'slug')
    date_hierarchy = 'created'
    list_filter = ('status',)
    search_fields = ('title', 'slug')


admin.site.register(Article, ArticleAdmin)