from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)

# Changing site's displayed name

admin.site.site_header = "Article Admin"
admin.site.site_title = "Article Admin Area"
admin.site.index_title = "Welcome to Article Admin Area"

