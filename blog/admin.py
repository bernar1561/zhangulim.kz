from django.contrib import admin
from .models import Article


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ["title", 'description']
