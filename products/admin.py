from django.contrib import admin
from . import models 

class ImageInline(admin.StackedInline):
    model = models.Image
    extra = 0
    min_num = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    # prepopulated_fields = {"slug": ("title",)} 
    
admin.site.register(models.Product, ProductAdmin) 
admin.site.register(models.Category)