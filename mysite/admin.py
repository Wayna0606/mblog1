from django.contrib import admin # type: ignore
from mysite.models import Post # type: ignore

class PostAdmin(admin.ModelAdmin):
    List_display = ('title', 'slug', 'pub_date')
admin.site.register(Post, PostAdmin)

