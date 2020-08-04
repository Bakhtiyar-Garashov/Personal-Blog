from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
prepopulated_fields = {'slug': ('title',), }
