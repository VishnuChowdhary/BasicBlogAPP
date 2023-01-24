from django.contrib import admin
from .models import *

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_filter = ['updated']
    search_fields = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
