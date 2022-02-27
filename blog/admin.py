from django.contrib import admin

from blog.forms import TagForm
from blog.models import Article, Tag

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm


# Changing site's displayed name

admin.site.site_header = "Blog admin area"
admin.site.site_title = "Blog admin area"
admin.site.index_title = "Welcome to the blog's admin area"
