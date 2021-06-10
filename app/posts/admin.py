from django.contrib import admin

from posts.models import Author, Article

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'active','created_at', 'updated_at']
    list_display_links = ['name']
    fields = ['name', 'picture', 'active']
    search_fields = ['name']
    list_filter = ['active']
    list_per_page = 12
    ordering = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'summary', 'author', 'active','created_at', 'updated_at']
    list_display_links = ['title', 'category']
    fields = ['title', 'category', 'summary', 'author', 'active', 'first_paragraph', 'body']
    search_fields = ['title', 'category']
    list_filter = ['active']
    list_per_page = 12
    ordering = ['title']
