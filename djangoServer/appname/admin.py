from django.contrib import admin

# Register your models here.

from django.contrib import admin
from appname.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # haha？
    list_display = ['title', 'content', 'time']


admin.site.register(Article ,ArticleAdmin)



