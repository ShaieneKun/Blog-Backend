from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)

# Changing site's displayed name

admin.site.site_header = "Blog admin area"
admin.site.site_title = "Blog admin area"
admin.site.index_title = "Welcome to the blog's admin area"