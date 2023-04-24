from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_editable = ('published',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('published',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('author',)
    list_editable = ('published',)

class NewsletterUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_email', 'added_at',)
    list_display_links = ('user_email',)
    search_fields = ('user_email',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(NewsletterUser, NewsletterUserAdmin)
