from django.contrib import admin
from django.db import models
import admin_thumbnails

from .models import Product, ProductGallery, Variation, ReviewRating
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'created_date', 'modified_date', )
    prepopulated_fields = {'slug': ('product_name', )}
    inlines = [ProductGalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', )
    list_editable = ('is_active', )
    list_filter = ('product', 'variation_category', 'variation_value', )

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)