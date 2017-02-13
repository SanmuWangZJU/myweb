from django.contrib import admin
from .models import Article

#定义自己的admin显示形式
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)

# Register your models here.
admin.site.register(Article,ArticleAdmin)
