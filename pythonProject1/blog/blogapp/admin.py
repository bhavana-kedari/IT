from django.contrib import admin
import site
from blogapp.models import BlogPost

# Register your models here.

import models 
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    admin.site.register(models.BlogPost,BlogPostAdmin)

